const attributeOptions = {

    power_state: {
        ds: [
            "DSPowerState.OFF",
            "DSPowerState.UPS",
            "DSPowerState.FULL_POWER",
            "DSPowerState.LOW_POWER",
            "DSPowerState.UNKNOWN"
        ],

        spf: [
            "SPFPowerState.UNKNOWN",
            "SPFPowerState.LOW_POWER",
            "SPFPowerState.FULL_POWER"
        ],

        spfrx: []
    },

    capability_state: {

        ds_1: [
            "DSOperatingMode.UNKNOWN",
            "DSOperatingMode.STARTUP",
            "DSOperatingMode.STANDBY",
            "DSOperatingMode.STOW",
            "DSOperatingMode.LOCKED",
            "DSOperatingMode.POINT"
        ],

        ds_2: [
            "IndexerPosition.OPTICAL",
            "IndexerPosition.B1",
            "IndexerPosition.B2",
            "IndexerPosition.B3",
            "IndexerPosition.B4",
            "IndexerPosition.B5",
            "IndexerPosition.B6",
            "IndexerPosition.MOVING",
            "IndexerPosition.UNKNOWN",
            "IndexerPosition.ERROR"
        ],

        ds_3: [
            "DishMode.STARTUP",
            "DishMode.SHUTDOWN",
            "DishMode.STANDBY_LP",
            "DishMode.STANDBY_FP",
            "DishMode.MAINTENANCE",
            "DishMode.STOW",
            "DishMode.CONFIG",
            "DishMode.OPERATE",
            "DishMode.UNKNOWN"
        ],

        spf: [
            "SPFCapabilityStates.UNAVAILABLE",
            "SPFCapabilityStates.STANDBY",
            "SPFCapabilityStates.OPERATE_DEGRADED",
            "SPFCapabilityStates.OPERATE_FULL"
        ],

        spfrx: [
            "SPFRxCapabilityStates.UNKNOWN",
            "SPFRxCapabilityStates.OPERATE",
            "SPFRsCapabilityStates.UNAVAILABLE",
            "SPFRxCapabilityStates.STANDBY",
            "SPFRxCapabilityStates.CONFIGURE"
        ]
    },

    configured_band: {

        ds: [
            "IndexerPosition.OPTICAL",
            "IndexerPosition.B1",
            "IndexerPosition.B2",
            "IndexerPosition.B3",
            "IndexerPosition.B4",
            "IndexerPosition.B5",
            "IndexerPosition.B6",
            "IndexerPosition.MOVING",
            "IndexerPosition.UNKNOWN",
            "IndexerPosition.ERROR"
        ],

        spf: [
            "SPFBandInFocus.UNKNOWN",
            "SPFBandInFocus.B1",
            "SPFBandInFocus.B2",
            "SPFBandInFocus.B3",
            "SPFBandInFocus.B4",
            "SPFBandInFocus.B5a",
            "SPFBandInFocus.B5b"
        ],

        spfrx: [
            "Band.NONE",
            "Band.B1",
            "Band.B2",
            "Band.B3",
            "Band.B4",
            "Band.B5a",
            "Band.B5b",
            "Band.UNKNOWN"
        ]
    },

    dish_mode: {

        ds_4: [
            "DSOperatingMode.UNKNOWN",
            "DSOperatingMode.STARTUP",
            "DSOperatingMode.STANDBY",
            "DSOperatingMode.STOW",
            "DSOperatingMode.LOCKED",
            "DSOperatingMode.POINT"
        ],

        ds_5: [
            "IndexerPosition.OPTICAL",
            "IndexerPosition.B1",
            "IndexerPosition.B2",
            "IndexerPosition.B3",
            "IndexerPosition.B4",
            "IndexerPosition.B5",
            "IndexerPosition.B6",
            "IndexerPosition.MOVING",
            "IndexerPosition.UNKNOWN",
            "IndexerPosition.ERROR"
        ],

        ds_6: [
            "DSPowerState.OFF",
            "DSPowerState.UPS",
            "DSPowerState.FULL_POWER",
            "DSPowerState.LOW_POWER",
            "DSPowerState.UNKNOWN"
        ],

        spf: [
            "SPFOperatingMode.UNKNOWN",
            "SPFOperatingModes.STARTUP",
            "SPFOperatingMode.STANDBY_LP",
            "SPFOperatingMode.OPERATE",
            "SPFOperatingMode.MAINTENANCE",
            "SPFOperatingMode.ERROR"
        ],

        spfrx: [
            "SPFRxOperatingMode.UNKNOWN",
            "SPFRxOperatingModes.STARTUP",
            "SPFRxOperatingMode.STANDBY",
            "SPFRxOperatingMode.OPERATE",
            "SPFRxOperatingMode.CONFIGURE"
        ]
    },

    health_state: {

        ds: [
            "HealthState.OK",
            "HealthState.DEGRADED",
            "HealthState.FAILED",
            "HealthState.UNKNOWN"
        ],

        spf: [
            "HealthState.NORMAL",
            "HealthState.DEGRADED",
            "HealthState.FAILED",
            "HealthState.UNKNOWN"
        ],

        spfrx: [
            "HealthState.OK",
            "HealthState.DEGRADED",
            "HealthState.FAILED",
            "HealthState.UNKNOWN"
        ]
    }
};


// ---------------------------------
// Elements
// ---------------------------------

const attributeSelect = document.getElementById("attribute-select");

const dsSelects = {

    normal: document.getElementById("ds-select"),

    capability: [
        document.getElementById("ds-select-1"),
        document.getElementById("ds-select-2"),
        document.getElementById("ds-select-3")
    ],

    dishMode: [
        document.getElementById("ds-select-4"),
        document.getElementById("ds-select-5"),
        document.getElementById("ds-select-6")
    ]
};

const dsCapabilityContainer =
    document.getElementById("ds-capability-container");

const dsDishModeContainer =
    document.getElementById("ds-dish-mode-container");

const spfSelect = document.getElementById("spf-select");
const spfrxSelect = document.getElementById("spfrx-select");

const ignoreSpfCheckbox =
    document.getElementById("ignore-spf");

const ignoreSpfrxCheckbox =
    document.getElementById("ignore-spfrx");

const spfGroup =
    document.getElementById("spf-group");

const spfrxGroup =
    document.getElementById("spfrx-group");


// ---------------------------------
// Dropdown helpers
// ---------------------------------

function populateDropdown(selectElement, values) {

    selectElement.innerHTML = "";

    values.forEach(value => {

        const option = document.createElement("option");

        option.value = value;
        option.textContent = value;

        selectElement.appendChild(option);
    });
}


function clearDropdown(selectElement) {

    selectElement.innerHTML = "";

    const option = document.createElement("option");

    option.value = "";
    option.textContent = "";

    selectElement.appendChild(option);
}


// ---------------------------------
// Update DS dropdowns
// ---------------------------------

function updateDropdowns() {

    const attribute = attributeSelect.value;
    const config = attributeOptions[attribute];

    // Hide all DS dropdown layouts
    dsSelects.normal.style.display = "none";
    dsCapabilityContainer.style.display = "none";
    dsDishModeContainer.style.display = "none";


    // Capability state
    if (attribute === "capability_state") {

        dsCapabilityContainer.style.display = "block";

        dsSelects.capability.forEach((select, index) => {

            populateDropdown(
                select,
                config[`ds_${index + 1}`]
            );
        });
    }


    // Dish mode
    else if (attribute === "dish_mode") {

        dsDishModeContainer.style.display = "block";

        dsSelects.dishMode.forEach((select, index) => {

            populateDropdown(
                select,
                config[`ds_${index + 4}`]
            );
        });
    }


    // Normal attributes
    else {

        dsSelects.normal.style.display = "block";

        populateDropdown(
            dsSelects.normal,
            config.ds
        );
    }

    updateVisibility();
}


// ---------------------------------
// Get DS values
// ---------------------------------

function getDsValues() {

    const attribute = attributeSelect.value;


    if (attribute === "capability_state") {

        return dsSelects.capability.map(
            select => select.value
        );
    }


    if (attribute === "dish_mode") {

        return dsSelects.dishMode.map(
            select => select.value
        );
    }


    return [dsSelects.normal.value];
}


// ---------------------------------
// SPF / SPFRx visibility
// ---------------------------------

function updateVisibility() {

    const config =
        attributeOptions[attributeSelect.value];


    // SPF
    if (ignoreSpfCheckbox.checked) {

        spfGroup.style.display = "none";

        clearDropdown(spfSelect);
    }

    else {

        spfGroup.style.display = "block";

        populateDropdown(
            spfSelect,
            config.spf
        );
    }


    // SPFRx
    if (ignoreSpfrxCheckbox.checked) {

        spfrxGroup.style.display = "none";

        clearDropdown(spfrxSelect);
    }

    else {

        spfrxGroup.style.display = "block";

        populateDropdown(
            spfrxSelect,
            config.spfrx
        );
    }
}


// ---------------------------------
// Render result
// ---------------------------------

function renderResult(result) {

    const resultSpan =
        document.querySelector(".result-item span");

    const ruleSpan =
        document.querySelectorAll(".result-item span")[1];

    resultSpan.textContent = result.result;

    ruleSpan.textContent = result.matched_rule;


    const whyBlock =
        document.querySelector(".result-block");

    whyBlock.innerHTML = "<strong>Reason:</strong>";


    const pWhyBlock =
        document.createElement("p");

    pWhyBlock.textContent =
        result.description;

    whyBlock.appendChild(pWhyBlock);
}


// ---------------------------------
// Calculate
// ---------------------------------

async function calculateResult() {

    const payload = {

        attribute: attributeSelect.value,

        ds: getDsValues(),

        spf: spfSelect.value,

        spfrx: spfrxSelect.value,

        ignoreSpf: ignoreSpfCheckbox.checked,

        ignoreSpfrx: ignoreSpfrxCheckbox.checked
    };


    console.log("Payload:", payload);


    const response = await fetch("/calculate", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(payload)
    });


    if (!response.ok) {

        const errorText =
            await response.text();

        console.error(
            "Server error:",
            errorText
        );

        return;
    }


    const result =
        await response.json();

    renderResult(result);
}


// ---------------------------------
// Header navigation
// ---------------------------------

const currentPath =
    window.location.pathname;

document
    .querySelectorAll(".header-link")
    .forEach(link => {

        const linkPath =
            link.getAttribute("href");

        link.classList.toggle(
            "active",
            linkPath === currentPath
        );
    });


// ---------------------------------
// Event listeners
// ---------------------------------

attributeSelect.addEventListener(
    "change",
    updateDropdowns
);

ignoreSpfCheckbox.addEventListener(
    "change",
    updateVisibility
);

ignoreSpfrxCheckbox.addEventListener(
    "change",
    updateVisibility
);

document
    .querySelector(".calculate-btn")
    .addEventListener(
        "click",
        calculateResult
    );


// ---------------------------------
// Initial setup
// ---------------------------------

updateDropdowns();