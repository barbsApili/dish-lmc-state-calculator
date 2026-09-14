# This implementation was developed with reference to the SKAO Dish LMC
# class, particularly its predefined state aggregation rules and processing
# logic. The calculator is an independent implementation for analysis and
# simulation purposes (https://gitlab.com/ska-telescope/mid-dish/ska-mid-dish-manager/-/blob/main/src/ska_mid_dish_manager/models/dish_state_transition.py?ref_type=heads).

"""State transition computation."""

from typing import Optional
from rule_engine.errors import (AttributeResolutionError, SymbolResolutionError)


from app.models.enums import SPFBandInFocus, HealthState, SPFHealthState
from app.models.transition_rules import (
    band_focus_rules_all_devices,
    band_focus_rules_spfrx_ignored,
    cap_state_rules_all_devices,
    cap_state_rules_ds_only,
    cap_state_rules_spf_ignored,
    cap_state_rules_spfrx_ignored,
    config_rules_all_devices,
    config_rules_ds_only,
    config_rules_spf_ignored,
    config_rules_spfrx_ignored,
    dish_mode_rules_all_devices,
    dish_mode_rules_ds_only,
    dish_mode_rules_spf_ignored,
    dish_mode_rules_spfrx_ignored,
    health_state_rules_all_devices,
    health_state_rules_ds_only,
    health_state_rules_spf_ignored,
    health_state_rules_spfrx_ignored,
    power_state_rules_all_devices,
    power_state_rules_spf_ignored,
)
from app.utils.calculation_result import CalculationResult

class StateTransition:
    """Computes the next state from rules based on component updates."""

    def compute_dish_mode(
        self,
        ds_component_state: dict = None,  # type: ignore
        spfrx_component_state: Optional[dict] = None,  # type: ignore
        spf_component_state: Optional[dict] = None,  # type: ignore
    ) -> CalculationResult:
        """Compute the dishMode based off component_states.
        :param ds_component_state: DS device component state
        :type ds_component_state: dict
        :param spfrx_component_state: SPFRX device component state
        :type spfrx_component_state: dict
        :param spf_component_state: SPF device component state
        :type spf_component_state: dict
        :return: the calculated dishMode
        :rtype: DishMode.
        """
        dish_manager_states = self._collapse(
            ds_component_state, spfrx_component_state, spf_component_state
        )
        rules_to_use = dish_mode_rules_ds_only
        if spfrx_component_state and spf_component_state:
            rules_to_use = dish_mode_rules_all_devices          
        elif spf_component_state:
            rules_to_use = dish_mode_rules_spfrx_ignored
        elif spfrx_component_state:
            rules_to_use = dish_mode_rules_spf_ignored
        for mode, rule_data in rules_to_use.items():
            rule = rule_data["rule"]
            if rule.matches(dish_manager_states):
                return CalculationResult(
                    result=mode,
                    matched_rule=mode,
                    description=rule_data["description"]
                )
        return CalculationResult(
            result="UNKNOWN",
            matched_rule="No Match", # Rule name
            description="Dish Mode aggregation is UNKNOWN because the supplied combination of subsystem states does not match any defined transition rule."
        )


    def compute_dish_health_state(
        self,
        ds_component_state: dict,  # type: ignore
        spfrx_component_state: Optional[dict] = None,  # type: ignore
        spf_component_state: Optional[dict] = None,  # type: ignore
        b5dc_component_state: Optional[dict] = None,  # type: ignore
    ) -> HealthState:
        """Compute the HealthState based off component states."""

        dish_manager_states = self._collapse(
            ds_component_state,
            spfrx_component_state,
            spf_component_state,
        )

        # Get the current healthState enum
        if ds_component_state:
            dish_manager_states["DS"]["healthstate"] = (
                ds_component_state.get("healthstate") or HealthState.UNKNOWN
            )

        if spfrx_component_state:
            dish_manager_states["SPFRX"]["healthstate"] = (
                spfrx_component_state.get("healthstate") or HealthState.UNKNOWN
            )

        if spf_component_state:
            dish_manager_states["SPF"]["healthstate"] = (
                spf_component_state.get("healthstate") or SPFHealthState.UNKNOWN
            )

        def normalise_health_state(value, enum_class):
            """Convert a health state value into the format used by rules."""

            if isinstance(value, list):
                value = value[0]

            if isinstance(value, enum_class):
                return value.name

            if isinstance(value, str):
                return value.split(".")[-1]

            return enum_class(value).name


        # DS is always included
        ds_healthstate_name = normalise_health_state(
            dish_manager_states["DS"]["healthstate"],
            HealthState,
        )
        dish_manager_states["DS"]["healthstate"] = (
            f"HealthState.{ds_healthstate_name}"
        )

        # Only normalise SPFRX if it is being used
        if spfrx_component_state:
            spfrx_healthstate_name = normalise_health_state(
                dish_manager_states["SPFRX"]["healthstate"],
                HealthState,
            )
            dish_manager_states["SPFRX"]["healthstate"] = (
                f"HealthState.{spfrx_healthstate_name}"
            )

        # Only normalise SPF if it is being used
        if spf_component_state:
            spf_healthstate_name = normalise_health_state(
                dish_manager_states["SPF"]["healthstate"],
                SPFHealthState,
            )
            dish_manager_states["SPF"]["healthstate"] = (
                f"SPFHealthState.{spf_healthstate_name}"
            )
        rules_to_use = health_state_rules_ds_only

        if spfrx_component_state and spf_component_state:
            rules_to_use = health_state_rules_all_devices
        elif spf_component_state:
            rules_to_use = health_state_rules_spfrx_ignored
        elif spfrx_component_state:
            rules_to_use = health_state_rules_spf_ignored

        for healthstate, rule_data in rules_to_use.items():
            rule = rule_data["rule"]

            if rule.matches(dish_manager_states):
                return CalculationResult(
                    result=HealthState[healthstate].name,
                    matched_rule=healthstate,
                    description=rule_data["description"],
                )

        return CalculationResult(
            result=HealthState.UNKNOWN,
            matched_rule="No Match",
            description=(
                "Health State aggregation is UNKNOWN because the supplied "
                "combination of subsystem states does not match any defined "
                "transition rule."
            ),
        )
    
        # pylint: disable=too-many-arguments
    def compute_capability_state(
            self,
            ds_component_state: dict = None,  # type: ignore
            dish_manager_component_state: dict = None,  # type: ignore
            spfrx_component_state: Optional[dict] = None,  # type: ignore
            spf_component_state: Optional[dict] = None,  # type: ignore
        )-> CalculationResult:
            """Compute the capabilityState based off component_states.

            The same rules are used regardless of band.
            This method renames b5aCapabilityState to capabilitystate to
            apply the generic rules.

            :param band: The band to calculate for
            :type band: str
            :param ds_component_state: DS device component state
            :type ds_component_state: dict
            :param spfrx_component_state: SPFRX device component state
            :type spfrx_component_state: dict
            :param spf_component_state: SPF device component state
            :type spf_component_state: dict
            :param dish_manager_component_state: Dish Manager device component state
            :type dish_manager_component_state: dict
            :return: the calculated capabilityState
            :rtype: CapabilityStates
            """


            dish_manager_states = self._collapse(
                ds_component_state,
                spfrx_component_state,
                spf_component_state,
                dish_manager_component_state,
            )
            rules_to_use = cap_state_rules_ds_only
            if spfrx_component_state and spf_component_state:
                rules_to_use = cap_state_rules_all_devices
            elif spf_component_state:
                rules_to_use = cap_state_rules_spfrx_ignored
            elif spfrx_component_state:
                rules_to_use = cap_state_rules_spf_ignored

            new_cap_state = "UNKNOWN"
            rule_used = "-"
            for capability_state, rule_data in rules_to_use.items():
                try:
                    rule = rule_data["rule"]
                    if rule.matches(dish_manager_states):
                        if capability_state.startswith("STANDBY"):
                            new_cap_state = "STANDBY"
                        else:
                            new_cap_state = capability_state

                        rule_used = capability_state
                        break

                except AttributeResolutionError,SymbolResolutionError:
                    continue

            # Clean up state dicts
            for state_dict in [
                spfrx_component_state,
                spf_component_state,
                dish_manager_component_state,
            ]:
                if state_dict and "capabilitystate" in state_dict:
                    del state_dict["capabilitystate"]

            return CalculationResult(
                result=f"Capability State is {new_cap_state}",
                matched_rule=new_cap_state if new_cap_state !="UNKNOWN" else "No Match",
                description= "Capability State aggregation is UNKNOWN because the supplied combination of subsystem states does not match any defined transition rule." if new_cap_state == "UNKNOWN" else rule_data["description"]
                    )

    def compute_configured_band(
        self,
        ds_component_state: dict,  # type: ignore
        spfrx_component_state: Optional[dict] = None,  # type: ignore
        spf_component_state: Optional[dict] = None,  # type: ignore
    ) -> CalculationResult:
        """Compute the configuredband based off component_states.

        :param ds_component_state: DS device component state
        :type ds_component_state: dict
        :param spfrx_component_state: SPFRX device component state
        :type spfrx_component_state: dict
        :param spf_component_state: SPF device component state
        :type spf_component_state: dict
        :return: the calculated configuredband
        :rtype: Band
        """
        dish_manager_states = self._collapse(
            ds_component_state, spfrx_component_state, spf_component_state
        )
        rules_to_use = config_rules_ds_only
        if spfrx_component_state and spf_component_state:
            rules_to_use = config_rules_all_devices
        elif spf_component_state:
            rules_to_use = config_rules_spfrx_ignored
        elif spfrx_component_state:
            rules_to_use = config_rules_spf_ignored
        for band_number, rule_data in rules_to_use.items():
            rule = rule_data["rule"]
            if rule.matches(dish_manager_states):
                return CalculationResult(
                    result=f"Band.{band_number}",
                    matched_rule=band_number,
                    description=rule_data["description"]
                )
        return CalculationResult(
            result="UNKNOWN",
            matched_rule="No Match",
            description="Configured Band aggregation is UNKNOWN because the supplied combination of subsystem states does not match any defined transition rule."
        )

    def compute_spf_band_in_focus(
        self,
        ds_component_state: dict = None,  # type: ignore
        spfrx_component_state: Optional[dict] = None,  # type: ignore
    ) -> CalculationResult:
        """Compute the bandinfocus based off component_states.

        :param ds_component_state: DS device component state
        :type ds_component_state: dict
        :param spfrx_component_state: SPFRX device component state
        :type spfrx_component_state: dict
        :return: the calculated bandinfocus
        :rtype: SPFBandInFocus
        """
        dish_manager_states = self._collapse(ds_component_state, spfrx_component_state)
        rules_to_use = band_focus_rules_all_devices
        if not spfrx_component_state:
            rules_to_use = band_focus_rules_spfrx_ignored

        for band_number, rule_data in rules_to_use.items():
            if rule.matches(dish_manager_states):
                rule = rule_data["rule"]
                return CalculationResult(
                    result=SPFBandInFocus[band_number],
                    matched_rule=SPFBandInFocus[band_number],
                    description=rule_data["description"]
                )

        return CalculationResult(
            result= "UNKNOWN",
            matched_rule="No Match",
            description="SPF Band in Focus's aggregation is UNKNOWN because the supplied combination of subsystem states does not match any defined transition rule.",
        )

    def compute_power_state(
        self,
        ds_component_state: dict = None,  # type: ignore
        spf_component_state: Optional[dict] = None,  # type: ignore
    ) -> CalculationResult:
        """Compute the powerstate based off component_states.

        :param ds_component_state: DS device component state
        :type ds_component_state: dict
        :param spf_component_state: SPF device component state
        :type spf_component_state: dict
        :return: the calculated powerstate
        :rtype: PowerState
        """
        dish_manager_states = self._collapse(
            ds_component_state, spf_component_state=spf_component_state
        )
        rules_to_use = power_state_rules_all_devices
        if not spf_component_state:
            rules_to_use = power_state_rules_spf_ignored

        for power_state, rule_data in rules_to_use.items():
            rule = rule_data["rule"]
            if rule.matches(dish_manager_states):
                normalized_state = (
                    power_state.split("_")[0]
                    if "_" in power_state
                    else power_state
                )

                return CalculationResult(
                    result=normalized_state,
                    matched_rule=power_state,
                    description=rule_data["description"],
                )

    @classmethod
    def _collapse(
        cls,
        ds_component_state: dict = None,  # type: ignore
        spfrx_component_state: Optional[dict] = None,
        spf_component_state: Optional[dict] = None,  # type: ignore
        dish_manager_component_state: Optional[dict] = None,  # type: ignore
    ) -> dict:  # type: ignore
        """Collapse multiple state dicts into one."""
        dish_manager_states = {"DS": {}}  # type: ignore

        for key, val in ds_component_state.items():
            if isinstance(val, list) and len(val) == 1:
                val = val[0]

            dish_manager_states["DS"][key] = str(val)

        if spfrx_component_state:
            dish_manager_states["SPFRX"] = {}
            for key, val in spfrx_component_state.items():
                dish_manager_states["SPFRX"][key] = str(val)

        if spf_component_state:
            dish_manager_states["SPF"] = {}
            for key, val in spf_component_state.items():
                dish_manager_states["SPF"][key] = str(val)

        if dish_manager_component_state:
            dish_manager_states["DM"] = {}
            for key, val in dish_manager_component_state.items():
                dish_manager_states["DM"][key] = str(val)

        return dish_manager_states
