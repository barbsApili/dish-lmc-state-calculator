const stateOptions = {

    power_state: {
        state: [
            "UPS",
            "LOW",
            "FULL"
        ]
    },

    capability_state: {
        state: [
            "UNAVAILABLE",
            "STANDBY",
            "OPERATE_FULL",
            "CONFIGURING",
            "OPERATE_DEGRADED"
        ]
    },

    configured_band: {
        state: [
            "NONE",
            "B1",
            "B2",
            "B3",
            "B4",
            "B5",
            "B5a",
            "B5b",
            "MOVING",
            "UNKNOWN",
            "ERROR"
        ]
    },

    dish_mode: {
        state: [
            "STARTUP",
            "STOW",
            "CONFIG",
            "OPERATE",
            "STANDBY_LP",
            "STANDBY_FP"
        ]
    },

    health_state: {
        state: [
            "DEGRADED",
            "FAILED",
            "OK",
            "UNKNOWN"
        ]
    }
};


// =========================================================
// ELEMENTS
// =========================================================

const stateSelect = document.getElementById("attribute-select-reverse");
const stateDropdown = document.getElementById("ds-select-reverse");
const adviceButton = document.querySelector(".advise-btn");


// =========================================================
// NAVIGATION
// =========================================================

const currentPath = window.location.pathname;

document.querySelectorAll(".header-link").forEach(link => {

    const linkPath = link.getAttribute("href");

    link.classList.toggle("active", linkPath === currentPath);

});


// =========================================================
// DROPDOWNS
// =========================================================

function populateDropdown(dropdown, values) {

    dropdown.innerHTML = "";

    values.forEach(value => {

        const option = document.createElement("option");

        option.value = value;
        option.textContent = value;

        dropdown.appendChild(option);

    });
}


function updateDropdown() {

    const selectedState = stateSelect.value;
    const selectedOption = stateOptions[selectedState];

    populateDropdown(
        stateDropdown,
        selectedOption.state
    );
}


// =========================================================
// RENDER ADVICE
// =========================================================

function renderAdvice(response) {

    const spans = [
        document.querySelector(".all-devices span"),
        document.querySelector(".spf-ignored span"),
        document.querySelector(".spfrx-ignored span"),
        document.querySelector(".ds-only span")
    ];

    response.forEach((scenario, index) => {

        const span = spans[index];

        if (scenario == null) {

            span.innerHTML = "";

            return;
        }

        if (Array.isArray(scenario)) {

            let result = "";

            scenario.forEach((element, caseIndex) => {

                result += `
                    <br><br><b>Case ${caseIndex + 1}</b><br><br>
                    ${element}<br><br>
                `;

            });

            span.innerHTML = result;

            return;
        }

        span.innerHTML = scenario;

    });
}


// =========================================================
// ADVICE
// =========================================================

function advise(response) {

    renderAdvice(response.advice);

}


// =========================================================
// ADVICE BUTTON
// =========================================================

adviceButton.addEventListener("click", async () => {

    const selectedState = stateSelect.value;
    const selectedMode = stateDropdown.value;

    const response = await fetch(
        `/reverse/advice/${selectedState}/${selectedMode}`
    );

    const data = await response.json();

    advise(data);

});


// =========================================================
// EVENT LISTENERS
// =========================================================

stateSelect.addEventListener("change", updateDropdown);

updateDropdown();