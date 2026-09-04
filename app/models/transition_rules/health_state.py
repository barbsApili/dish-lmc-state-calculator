# This implementation was developed with reference to the SKAO Dish LMC
# class, particularly its predefined state aggregation rules.
# The calculator is an independent implementation for analysis and
# simulation purposes (https://gitlab.com/ska-telescope/mid-dish/ska-mid-dish-manager/-/tree/main/src/ska_mid_dish_manager/models/transition_rules?ref_type=heads) 

"""Automatic transition rules for health state."""

import rule_engine


# NOTE! The following healthState computations apply under the assumption
# that all components/subdevices that DishLMC is expected to monitor & control
# are available and that connection with those components is ESTABLISHED.
#
# If a component is expected and its communicationState is DISABLED or
# NOT_ESTABLISHED, the computed dish healthState will be overwritten to
# report FAILED.


HEALTH_STATE_RULES_ALL_DEVICES = {
    "DEGRADED": {
        "rule": rule_engine.Rule(
            "("
            "DS.healthstate == 'HealthState.DEGRADED' and "
            "SPF.healthstate in "
            "['SPFHealthState.NORMAL', "
            " 'SPFHealthState.DEGRADED', "
            " 'SPFHealthState.UNKNOWN'] "
            "and "
            "SPFRX.healthstate in "
            "['HealthState.OK', "
            " 'HealthState.DEGRADED', "
            " 'HealthState.UNKNOWN']"
            ") "
            "or "
            "("
            "DS.healthstate in "
            "['HealthState.OK', "
            " 'HealthState.DEGRADED', "
            " 'HealthState.UNKNOWN'] "
            "and "
            "SPF.healthstate == 'SPFHealthState.DEGRADED' "
            "and "
            "SPFRX.healthstate in "
            "['HealthState.OK', "
            " 'HealthState.DEGRADED', "
            " 'HealthState.UNKNOWN']"
            ") "
            "or "
            "("
            "DS.healthstate in "
            "['HealthState.OK', "
            " 'HealthState.DEGRADED', "
            " 'HealthState.UNKNOWN'] "
            "and "
            "SPF.healthstate in "
            "['SPFHealthState.NORMAL', "
            " 'SPFHealthState.DEGRADED', "
            " 'SPFHealthState.UNKNOWN'] "
            "and "
            "SPFRX.healthstate == 'HealthState.DEGRADED'"
            ")"
        ),
        "description": (
            "Health state aggregated to DEGRADED because at least one "
            "of the Dish Structure, SPF, or SPFRX health states is DEGRADED "
            "while none of the components have a FAILED health state."
        ),
    },

    "FAILED": {
        "rule": rule_engine.Rule(
            "DS.healthstate == 'HealthState.FAILED' or "
            "SPF.healthstate == 'SPFHealthState.FAILED' or "
            "SPFRX.healthstate == 'HealthState.FAILED'"
        ),
        "description": (
            "Health state aggregated to FAILED because the Dish Structure, "
            "SPF, or SPFRX health state is FAILED."
        ),
    },

    "OK": {
        "rule": rule_engine.Rule(
            "DS.healthstate == 'HealthState.OK' and "
            "SPF.healthstate == 'SPFHealthState.NORMAL' and "
            "SPFRX.healthstate == 'HealthState.OK'"
        ),
        "description": (
            "Health state aggregated to OK because the Dish Structure "
            "health state is OK, the SPF health state is NORMAL, and "
            "the SPFRX health state is OK."
        ),
    },

    "UNKNOWN": {
        "rule": rule_engine.Rule(
            "DS.healthstate == 'HealthState.UNKNOWN' or "
            "SPF.healthstate == 'SPFHealthState.UNKNOWN' or "
            "SPFRX.healthstate == 'HealthState.UNKNOWN'"
        ),
        "description": (
            "Health state aggregated to UNKNOWN because the Dish Structure, "
            "SPF, or SPFRX health state is UNKNOWN."
        ),
    },
}


HEALTH_STATE_RULES_SPF_IGNORED = {
    "DEGRADED": {
        "rule": rule_engine.Rule(
            "("
            "DS.healthstate == 'HealthState.DEGRADED' and "
            "SPFRX.healthstate in "
            "['HealthState.OK', "
            " 'HealthState.DEGRADED', "
            " 'HealthState.UNKNOWN']"
            ") "
            "or "
            "("
            "DS.healthstate in "
            "['HealthState.OK', "
            " 'HealthState.DEGRADED', "
            " 'HealthState.UNKNOWN'] "
            "and "
            "SPFRX.healthstate == 'HealthState.DEGRADED'"
            ")"
        ),
        "description": (
            "Health state aggregated to DEGRADED because the Dish Structure "
            "or SPFRX health state is DEGRADED while the other component "
            "is not FAILED, and SPF inputs are ignored."
        ),
    },

    "FAILED": {
        "rule": rule_engine.Rule(
            "DS.healthstate == 'HealthState.FAILED' or "
            "SPFRX.healthstate == 'HealthState.FAILED'"
        ),
        "description": (
            "Health state aggregated to FAILED because the Dish Structure "
            "or SPFRX health state is FAILED, and SPF inputs are ignored."
        ),
    },

    "OK": {
        "rule": rule_engine.Rule(
            "DS.healthstate == 'HealthState.OK' and "
            "SPFRX.healthstate == 'HealthState.OK'"
        ),
        "description": (
            "Health state aggregated to OK because the Dish Structure "
            "and SPFRX health states are OK, and SPF inputs are ignored."
        ),
    },

    "UNKNOWN": {
        "rule": rule_engine.Rule(
            "DS.healthstate == 'HealthState.UNKNOWN' or "
            "SPFRX.healthstate == 'HealthState.UNKNOWN'"
        ),
        "description": (
            "Health state aggregated to UNKNOWN because the Dish Structure "
            "or SPFRX health state is UNKNOWN, and SPF inputs are ignored."
        ),
    },
}


HEALTH_STATE_RULES_SPFRX_IGNORED = {
    "DEGRADED": {
        "rule": rule_engine.Rule(
            "("
            "DS.healthstate == 'HealthState.DEGRADED' and "
            "SPF.healthstate in "
            "['SPFHealthState.NORMAL', "
            " 'SPFHealthState.DEGRADED', "
            " 'SPFHealthState.UNKNOWN']"
            ") "
            "or "
            "("
            "DS.healthstate in "
            "['HealthState.OK', "
            " 'HealthState.DEGRADED', "
            " 'HealthState.UNKNOWN'] "
            "and "
            "SPF.healthstate == 'SPFHealthState.DEGRADED'"
            ")"
        ),
        "description": (
            "Health state aggregated to DEGRADED because the Dish Structure "
            "or SPF health state is DEGRADED while the other component "
            "is not FAILED, and SPFRX inputs are ignored."
        ),
    },

    "FAILED": {
        "rule": rule_engine.Rule(
            "DS.healthstate == 'HealthState.FAILED' or "
            "SPF.healthstate == 'SPFHealthState.FAILED'"
        ),
        "description": (
            "Health state aggregated to FAILED because the Dish Structure "
            "or SPF health state is FAILED, and SPFRX inputs are ignored."
        ),
    },

    "OK": {
        "rule": rule_engine.Rule(
            "DS.healthstate == 'HealthState.OK' and "
            "SPF.healthstate == 'SPFHealthState.NORMAL'"
        ),
        "description": (
            "Health state aggregated to OK because the Dish Structure "
            "health state is OK and the SPF health state is NORMAL, "
            "and SPFRX inputs are ignored."
        ),
    },

    "UNKNOWN": {
        "rule": rule_engine.Rule(
            "DS.healthstate == 'HealthState.UNKNOWN' or "
            "SPF.healthstate == 'SPFHealthState.UNKNOWN'"
        ),
        "description": (
            "Health state aggregated to UNKNOWN because the Dish Structure "
            "or SPF health state is UNKNOWN, and SPFRX inputs are ignored."
        ),
    },
}


HEALTH_STATE_RULES_DS_ONLY = {
    "DEGRADED": {
        "rule": rule_engine.Rule(
            "DS.healthstate == 'HealthState.DEGRADED'"
        ),
        "description": (
            "Health state aggregated to DEGRADED because the Dish Structure "
            "health state is DEGRADED, and SPF and SPFRX inputs are ignored."
        ),
    },

    "FAILED": {
        "rule": rule_engine.Rule(
            "DS.healthstate == 'HealthState.FAILED'"
        ),
        "description": (
            "Health state aggregated to FAILED because the Dish Structure "
            "health state is FAILED, and SPF and SPFRX inputs are ignored."
        ),
    },

    "OK": {
        "rule": rule_engine.Rule(
            "DS.healthstate == 'HealthState.OK'"
        ),
        "description": (
            "Health state aggregated to OK because the Dish Structure "
            "health state is OK, and SPF and SPFRX inputs are ignored."
        ),
    },

    "UNKNOWN": {
        "rule": rule_engine.Rule(
            "DS.healthstate == 'HealthState.UNKNOWN'"
        ),
        "description": (
            "Health state aggregated to UNKNOWN because the Dish Structure "
            "health state is UNKNOWN, and SPF and SPFRX inputs are ignored."
        ),
    },
}