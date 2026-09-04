

from collections import deque

from app.models.enums import DishMode


DISH_MODE_GRAPH = {
    DishMode.UNKNOWN: [
        {
            "target": DishMode.STARTUP,
            "condition": "Call STOW. No Power State Conditions."
            "NB: Only possible when normal operation has been restored",
        },
        {
            "target": DishMode.STOW,
            "condition":"Call STOW. No Power State Conditions"
            "NB: Only possible when normal operation has been restored",
        },
        {
            "target": DishMode.CONFIG,
            "condition": "Call STOW. No Power State Conditions"
            "NB: Only possible when normal operation has been restored",
        },   
        {
            "target": DishMode.STANDBY_LP,
            "condition": "Call STOW. No Power State Conditions"
            "NB: Only possible when normal operation has been restored",
        },
        {
            "target": DishMode.STANDBY_FP,
            "condition": "Call STOW. No Power State Conditions"
            "NB: Only possible when normal operation has been restored",
        },
        {
            "target": DishMode.SHUTDOWN,
            "condition":"Can transition to Shutdown from any mode when: (1) Unplanned interruptions"
            " to the Dish power supply( for Dish instances supplied by local UPS);"
            "(2) Planned interruptions to the Dish power supply. No Power State restriction."
        },
    ],

    DishMode.STARTUP: [
        {
            "target": DishMode.STANDBY_LP,
            "condition": "No Power State Conditions",
        },
        {
            "target": DishMode.STANDBY_FP,
            "condition": "Power State should be Full",
        },
        {
            "target": DishMode.STOW,
            "condition":"Can transition to STOW from any mode. Power State should be Low or Full",
        },
        {
            "target": DishMode.UNKNOWN,
            "condition":"Can transition to Unknown from any mode. Power State should be Low or Full",
        },
        {
            "target": DishMode.SHUTDOWN,
            "condition":"Can transition to Shutdown from any mode when: (1) Unplanned interruptions"
            " to the Dish power supply( for Dish instances supplied by local UPS);"
            "(2) Planned interruptions to the Dish power supply. No Power State restriction",
        },
    ],
    DishMode.STANDBY_LP: [
        {
            "target": DishMode.CONFIG,
            "condition": "Power State should be Full.",
        },
        {
            "target": DishMode.STANDBY_FP,
            "condition": "Power state FULL",
        },
        {
            "target": DishMode.STOW,
            "condition":"Can transition to STOW from any mode.",
        },
        {
            "target": DishMode.UNKNOWN,
            "condition":"Can transition to Unknown from any mode. Power State should be Low or Full",
        },
        {
            "target": DishMode.SHUTDOWN,
            "condition":"Can transition to Shutdown from any mode when: (1) Unplanned interruptions"
            " to the Dish power supply( for Dish instances supplied by local UPS);"
            "(2) Planned interruptions to the Dish power supply. No Power State restriction",
        },
    ],

    DishMode.STANDBY_FP: [
        {
            "target": DishMode.CONFIG,
            "condition": "No Power State Conditions",
        },
        {
            "target": DishMode.STANDBY_LP,
            "condition": "No Power State Conditions",
        },
        {
            "target": DishMode.STOW,
            "condition":"Can transition to STOW from any mode.",
        },
        {
            "target": DishMode.UNKNOWN,
            "condition":"Can transition to Unknown from any mode. Power State should be Low or Full",
        },
        {
            "target": DishMode.SHUTDOWN,
            "condition":"Can transition to Shutdown from any mode when: (1) Unplanned interruptions"
            " to the Dish power supply( for Dish instances supplied by local UPS);"
            "(2) Planned interruptions to the Dish power supply. No Power State restriction",
        },
    ],

    DishMode.CONFIG: [
        {
            "target": DishMode.STANDBY_LP,
            "condition": "No Power State Conditions",
        },
        {
            "target": DishMode.STANDBY_FP,
            "condition": "No Power State Conditions",
        },
        {
            "target": DishMode.OPERATE,
            "condition": "No Power State Conditions",
        },
        {
            "target": DishMode.UNKNOWN,
            "condition":"Can transition to Unknown from any mode. Power State should be Low or Full",
        },
        {
            "target": DishMode.SHUTDOWN,
            "condition":"Can transition to Shutdown from any mode when: (1) Unplanned interruptions"
            " to the Dish power supply( for Dish instances supplied by local UPS);"
            "(2) Planned interruptions to the Dish power supply. No Power State restriction",
        },
    ],

    DishMode.OPERATE: [
        {
            "target": DishMode.CONFIG,
            "condition": (
                "No Power State Conditions"
            ),
        },
        {
            "target": DishMode.STANDBY_LP,
            "condition": "Power State should be Full",
        },
        {
            "target": DishMode.STANDBY_FP,
            "condition": "No Power State Conditions",
        },
        {
            "target": DishMode.UNKNOWN,
            "condition":"Can transition to Unknown from any mode. Power State should be Low or Full",
        },
        {
            "target": DishMode.SHUTDOWN,
            "condition":"Can transition to Shutdown from any mode when: (1) Unplanned interruptions"
            " to the Dish power supply( for Dish instances supplied by local UPS);"
            "(2) Planned interruptions to the Dish power supply. No Power State restriction",
        },
        {
            "target": DishMode.STOW,
            "condition":"Can transition to STOW from any mode.",
        }
    ],

    DishMode.MAINTENANCE: [
        {
            "target": DishMode.STOW,
            "condition":"Can transition to STOW from any mode. Power State should be Low or Full",
        },
        {
            "target": DishMode.UNKNOWN,
            "condition":"Can transition to Unknown from any mode. Power State should be Low or Full",
        },
        {
            "target": DishMode.SHUTDOWN,
            "condition":"Can transition to Shutdown from any mode when: (1) Unplanned interruptions"
            " to the Dish power supply( for Dish instances supplied by local UPS);"
            "(2) Planned interruptions to the Dish power supply. No Power State restriction",
        },
    ],

    DishMode.STOW: [
        {
            "target": DishMode.STANDBY_FP,
            "condition": "No Power State Conditions",
        },
        {
            "target": DishMode.STANDBY_LP,
            "condition": "Power State must be Low",
        },
        {
            "target": DishMode.MAINTENANCE,
            "condition": "No Power State Conditions",
        },
        {
            "target": DishMode.UNKNOWN,
            "condition":"Can transition to Unknown from any mode. Power State should be Low or Full",
        },
        {
            "target": DishMode.SHUTDOWN,
            "condition":"Can transition to Shutdown from any mode when: (1) Unplanned interruptions"
            " to the Dish power supply( for Dish instances supplied by local UPS);"
            "(2) Planned interruptions to the Dish power supply. No Power State restriction",
        },
    ],
    DishMode.SHUTDOWN: [
        {
            "target": DishMode.STARTUP,
            "condition": "No Power State Conditions",
        },
    ],
}

def get_available_transitions(
    current_mode: DishMode,
    target_mode: DishMode,
):
    transitions = DISH_MODE_GRAPH.get(current_mode, [])

    possible_modes = [
        {
            "target": transition["target"].name,
            "condition": transition["condition"],
        }
        for transition in transitions
    ]

    # Direct transition exists
    for transition in transitions:
        if transition["target"] == target_mode:
            return {
                "one_hop":True,
                "current": current_mode.name,
                "target": target_mode.name,
                "direct": True,
                "condition": transition["condition"],
                "possible_modes": possible_modes,
                "paths": [],
            }

    # No direct transition - find paths
    paths = find_transition_paths(
        current_mode,
        target_mode,
    )

    return {
        "one_hop":False,
        "current": current_mode.name,
        "target": target_mode.name,
        "direct": False,
        "condition": (
            f"Cannot transition directly to "
            f"{target_mode.name} from {current_mode.name}"
        ),
        "possible_modes": possible_modes,
        "paths": [
            [
                {
                    "from": step["from"].name,
                    "to": step["to"].name,
                    "condition": step["condition"],
                }
                for step in path
            ]
            for path in paths
        ],
    }

def find_transition_paths(
    current_mode: DishMode,
    target_mode: DishMode,
    max_depth: int = 10,
):
    queue = deque([
        {
            "mode": current_mode,
            "steps": [],
        }
    ])

    paths = []

    while queue:
        item = queue.popleft()

        current = item["mode"]
        steps = item["steps"]

        if len(steps) >= max_depth:
            continue

        for transition in DISH_MODE_GRAPH.get(current, []):

            next_mode = transition["target"]

            # Prevent cycles
            if any(step["to"] == next_mode for step in steps):
                continue

            new_step = {
                "from": current,
                "to": next_mode,
                "condition": transition["condition"],
            }

            new_steps = steps + [new_step]

            # Target reached
            if next_mode == target_mode:
                paths.append(new_steps)

            else:
                queue.append({
                    "mode": next_mode,
                    "steps": new_steps,
                })

    return paths