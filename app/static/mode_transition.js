// =========================================================
// ELEMENTS
// =========================================================

const currentMode = document.getElementById("attribute-select-mode");
const targetMode = document.getElementById("ds-select-mode");
const modeButton = document.querySelector(".mode-btn");


// =========================================================
// NAVIGATION
// =========================================================

const currentPath = window.location.pathname;

document.querySelectorAll(".header-link").forEach(link => {

    const linkPath = link.getAttribute("href");

    link.classList.toggle("active", linkPath === currentPath);

});


// =========================================================
// TRANSITION PATH TOGGLE
// =========================================================

document.getElementById("transition-toggle").addEventListener("click", function() {

    document
        .getElementById("transition-content")
        .classList.toggle("show");

    this.classList.toggle("active");

});


// =========================================================
// RENDER MODES
// =========================================================

function renderModes(response) {

    const allowedModes = document.querySelector(".allowed-modes span");
    const possibleModes = document.querySelector(".possible-modes span");
    const altRoutes = document.querySelector(".alt-routes");

    const transitionPath = document.querySelector("#transition-path-section");


    // ---------------------------------------------------------
    // SHOW / HIDE TRANSITION PATH
    // ---------------------------------------------------------

    if (response.one_hop) {

        transitionPath.style.display = "none";

    } else {

        transitionPath.style.display = "block";

    }


    // ---------------------------------------------------------
    // TRANSITION RESULT
    // ---------------------------------------------------------

    const transitionText = `
        <strong>${response.current} → ${response.target}</strong><br><br>
        ${response.condition}<br><br>
    `;


    // ---------------------------------------------------------
    // AVAILABLE TRANSITIONS
    // ---------------------------------------------------------

    let possibleModesText = "";

    for (const mode of response.possible_modes) {

        possibleModesText += `
            <strong>${response.current} → ${mode.target}</strong><br><br>
            ${mode.condition}<br><br>
        `;

    }


    // ---------------------------------------------------------
    // TRANSITION PATH
    // ---------------------------------------------------------

    // Clear previous routes
    altRoutes.innerHTML = "";


    // Display the first two routes
    for (const [index, path] of response.paths.slice(0, 2).entries()) {


        // Create complete route

        const route = path
            .map(step => step.from)
            .concat(path[path.length - 1].to)
            .join(" → ");


        // Create option card

        const option = document.createElement("div");

        option.className = "route-option";


        // Option title

        const title = document.createElement("div");

        title.className = "route-option-title";
        title.textContent = `OPTION ${index + 1}`;

        option.appendChild(title);


        // Main route

        const routeElement = document.createElement("div");

        routeElement.className = "route-path";
        routeElement.textContent = route;

        option.appendChild(routeElement);


        // Create individual steps

        path.forEach((step, stepIndex) => {

            const stepElement = document.createElement("div");

            stepElement.className = "route-step";


            // Step number

            const stepNumber = document.createElement("div");

            stepNumber.className = "step-number";
            stepNumber.textContent = String(stepIndex + 1).padStart(2, "0");


            // Step content

            const stepContent = document.createElement("div");

            stepContent.className = "step-content";


            // Step transition

            const stepPath = document.createElement("div");

            stepPath.className = "step-path";
            stepPath.textContent = `${step.from} → ${step.to}`;


            // Condition

            const condition = document.createElement("div");

            condition.className = "step-condition";
            condition.textContent = step.condition;


            // Assemble step

            stepContent.appendChild(stepPath);
            stepContent.appendChild(condition);

            stepElement.appendChild(stepNumber);
            stepElement.appendChild(stepContent);

            option.appendChild(stepElement);

        });


        // Add option to route container

        altRoutes.appendChild(option);

    }


    // ---------------------------------------------------------
    // UPDATE RESULTS
    // ---------------------------------------------------------

    allowedModes.innerHTML = transitionText;
    possibleModes.innerHTML = possibleModesText;

}


// =========================================================
// MODE RESPONSE
// =========================================================

function getMode(response) {

    renderModes(response);

}


// =========================================================
// MODE BUTTON
// =========================================================

modeButton.addEventListener("click", async () => {

    const currentModeValue = currentMode.value;
    const targetModeValue = targetMode.value;

    const response = await fetch(
        `/transition/advice/${currentModeValue}/${targetModeValue}`
    );

    const data = await response.json();

    getMode(data);

});