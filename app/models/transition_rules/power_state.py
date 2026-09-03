"""Automatic transition rules for power state.

* The DSPowerState enumeration only has 2 labels in the latest ICD.
  This impacts the rules defined in this file.

* These rules assume that the DS power state has higher priority,
  while the SPF power state is supplementary.

TODO:
    Obtain clarification on the DSPowerState ICD definitions.
"""

import rule_engine  # type: ignore


POWER_STATE_RULES_ALL_DEVICES = {
    "UPS": {
        "rule": rule_engine.Rule(
            "DS.powerstate in "
            "['DSPowerState.UPS', 'DSPowerState.OFF']"
        ),
        "description": (
            "Power state aggregated to UPS because "
            "the Dish Structure's power state is UPS or OFF."
        ),
    },

    "LOW_1": {
        "rule": rule_engine.Rule(
            "DS.powerstate == 'DSPowerState.LOW_POWER'"
        ),
        "description": (
            "Power state aggregated to LOW because "
            "the Dish Structure's power state is LOW."
        ),
    },

    "FULL_1": {
        "rule": rule_engine.Rule(
            "DS.powerstate == 'DSPowerState.FULL_POWER'"
        ),
        "description": (
            "Power state aggregated to FULL POWER because "
            "the Dish Structure's power state is FULL."
        ),
    },

    # DS is UNKNOWN, therefore SPF is used as supplementary input.
    "LOW_2": {
        "rule": rule_engine.Rule(
            "DS.powerstate == 'DSPowerState.UNKNOWN' and "
            "SPF.powerstate == 'SPFPowerState.LOW_POWER'"
        ),
        "description": (
            "Power state aggregated to LOW because "
            "the Dish Structure's power state is UNKNOWN "
            "while the SPF power state is LOW."
        ),
    },

    "FULL_2": {
        "rule": rule_engine.Rule(
            "DS.powerstate == 'DSPowerState.UNKNOWN' and "
            "SPF.powerstate == 'SPFPowerState.FULL_POWER'"
        ),
        "description": (
            "Power state aggregated to FULL because "
            "the Dish Structure's power state is UNKNOWN "
            "while the SPF power state is FULL."
        ),
    },

    # Both subsystems report UNKNOWN.
    "LOW_3": {
        "rule": rule_engine.Rule(
            "DS.powerstate == 'DSPowerState.UNKNOWN' and "
            "SPF.powerstate == 'SPFPowerState.UNKNOWN'"
        ),
        "description": (
            "Power state aggregated conservatively to "
            "LOW because both the Dish Structure's "
            "power state and the SPF power state are UNKNOWN."
        ),
    },
}


POWER_STATE_RULES_SPF_IGNORED = {
    "UPS": {
        "rule": rule_engine.Rule(
            "DS.powerstate in "
            "['DSPowerState.UPS', 'DSPowerState.OFF']"
        ),
        "description": (
            "Power state aggregated to UPS because "
            "the Dish Structure's power state is UPS or OFF, "
            "while SPF inputs are ignored."
        ),
    },

    "LOW": {
        "rule": rule_engine.Rule(
            "DS.powerstate in "
            "['DSPowerState.LOW_POWER', "
            "'DSPowerState.UNKNOWN']"
        ),
        "description": (
            "Power state aggregated to LOW POWER because "
            "the Dish Structure's power state is LOW_POWER "
            "or UNKNOWN, while SPF inputs are ignored."
        ),
    },

    "FULL": {
        "rule": rule_engine.Rule(
            "DS.powerstate == 'DSPowerState.FULL_POWER'"
        ),
        "description": (
            "Power state aggregated to FULL POWER because "
            "the Dish Structure's power state is FULL_POWER, "
            "while SPF inputs are ignored."
        ),
    },
}