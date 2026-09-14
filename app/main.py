from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.models.enums import (
    Band,
    CapabilityStates,
    DishMode,
    HealthState,
    PowerState,
)
from app.models.state_graph.state_graph import get_available_transitions
from app.models.state_transitions import StateTransition
from app.models.transition_advice.capability_state_advice import (
    get_capability_state_advice,
)
from app.models.transition_advice.configured_band_advice import (
    get_configured_band_advice,
)
from app.models.transition_advice.dish_mode_advice import (
    get_dish_mode_advice,
)
from app.models.transition_advice.health_state_advice import (
    get_health_state_advice,
)
from app.models.transition_advice.power_state_advice import (
    get_power_state_advice,
)


app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request},
    )


@app.get("/reverse", response_class=HTMLResponse)
async def reverse(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="reverse.html",
        context={"request": request},
    )


@app.get("/transition", response_class=HTMLResponse)
async def transition(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="mode_transition.html",
        context={"request": request},
    )


@app.post("/calculate")
async def calculate(request: Request):
    data = await request.json()

    ds = data.get("ds")
    spf = data.get("spf") if not data.get("ignoreSpf") else {}
    spfrx = data.get("spfrx") if not data.get("ignoreSpfrx") else {}
    attribute = data.get("attribute")

    calc = StateTransition()
    result = None

    # POWER STATE
    if attribute == "power_state":
        ds_component_state = {
            "powerstate": ds[0],
        }

        spf_component_state = (
            {"powerstate": spf}
            if spf != ""
            else None
        )

        result = calc.compute_power_state(
            ds_component_state=ds_component_state,
            spf_component_state=spf_component_state,
        )

    # CAPABILITY STATE
    elif attribute == "capability_state":
        ds_component_state = {
            "operatingmode": ds[0],
            "indexerposition": ds[1],
        }

        spf_component_state = (
            {"capabilitystate": spf}
            if spf
            else {}
        )

        spfrx_component_state = (
            {"capabilitystate": spfrx}
            if spfrx
            else {}
        )

        dish_manager_component_state = {
            "dishmode": ds[2],
        }

        result = calc.compute_capability_state(
            ds_component_state=ds_component_state,
            dish_manager_component_state=dish_manager_component_state,
            spfrx_component_state=spfrx_component_state,
            spf_component_state=spf_component_state,
        )

    # CONFIGURED BAND
    elif attribute == "configured_band":
        ds_component_state = {
            "indexerposition": ds[0],
        }

        spf_component_state = (
            {"bandinfocus": spf}
            if spf != ""
            else None
        )

        spfrx_component_state = (
            {"configuredband": spfrx}
            if spfrx != ""
            else None
        )

        result = calc.compute_configured_band(
            ds_component_state=ds_component_state,
            spf_component_state=spf_component_state,
            spfrx_component_state=spfrx_component_state,
        )

    # DISH MODE
    elif attribute == "dish_mode":
        ds_component_state = {
            "operatingmode": ds[0],
            "indexerposition": ds[1],
            "powerstate": ds[2],
        }

        spf_component_state = (
            {"operatingmode": spf}
            if spf
            else {}
        )

        spfrx_component_state = (
            {"operatingmode": spfrx}
            if spfrx
            else {}
        )

        result = calc.compute_dish_mode(
            ds_component_state=ds_component_state,
            spfrx_component_state=spfrx_component_state,
            spf_component_state=spf_component_state,
        )

    # HEALTH STATE
    elif attribute == "health_state":
        ds_component_state = {
            "healthstate": ds,
        }

        spf_component_state = (
            {"healthstate": spf}
            if spf not in ("", {}, None)
            else None
        )

        spfrx_component_state = (
            {"healthstate": spfrx}
            if spfrx not in ("", {}, None)
            else None
        )

        result = calc.compute_dish_health_state(
            ds_component_state=ds_component_state,
            spf_component_state=spf_component_state,
            spfrx_component_state=spfrx_component_state,
        )

    return {
        "result": result.result,
        "matched_rule": str(result.matched_rule),
        "description": str(result.description),
    }


@app.get("/reverse/advice/{attribute}/{state}")
async def dish_mode_advice(attribute: str, state: str):
    match attribute:
        case "dish_mode":
            dish_mode = DishMode[state]

            return {
                "advice": get_dish_mode_advice(dish_mode),
            }

        case "power_state":
            power_state = PowerState[state]

            return {
                "advice": get_power_state_advice(power_state),
            }

        case "capability_state":
            capability_state = CapabilityStates[state]

            return {
                "advice": get_capability_state_advice(capability_state),
            }

        case "health_state":
            health_state = HealthState[state]

            return {
                "advice": get_health_state_advice(health_state),
            }

        case "configured_band":
            band = Band[state]

            return {
                "advice": get_configured_band_advice(band),
            }

        case _:
            return {"advice": "UNKNOWN"}


@app.get("/transition/advice/{current}/{target}")
async def transition_advice(current: str, target: str):
    transition = get_available_transitions(
        DishMode[current],
        DishMode[target],
    )

    return transition