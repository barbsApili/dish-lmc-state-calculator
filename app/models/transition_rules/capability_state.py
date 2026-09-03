"""Automatic transition rules for capability states."""

import rule_engine


CAPABILITY_STATE_RULES_ALL_DEVICES = {
    "UNAVAILABLE": {
        "rule": rule_engine.Rule(
            "(DS.operatingmode == 'DSOperatingMode.STARTUP' or "
            "DS.operatingmode == 'DSOperatingMode.ESTOP') "
            "and "
            "SPF.capabilitystate == 'SPFCapabilityStates.UNAVAILABLE' "
            "and "
            "SPFRX.capabilitystate == 'SPFRxCapabilityStates.UNAVAILABLE'"
        ),
        "description": (
            "Capability state aggregated to UNAVAILABLE because "
            "the Dish Structure's operating mode is STARTUP or ESTOP, "
            "the SPF capability state is UNAVAILABLE, and "
            "the SPFRX capability state is UNAVAILABLE."
        ),
    },

    "STANDBY_1": {
        "rule": rule_engine.Rule(
            "DM.dishmode in "
            "['DishMode.STANDBY_LP', 'DishMode.STANDBY_FP'] "
            "and "
            "SPF.capabilitystate in "
            "['SPFCapabilityStates.STANDBY', "
            "'SPFCapabilityStates.OPERATE_DEGRADED', "
            "'SPFCapabilityStates.OPERATE_FULL'] "
            "and "
            "SPFRX.capabilitystate in "
            "['SPFRxCapabilityStates.STANDBY', "
            "'SPFRxCapabilityStates.OPERATE']"
        ),
        "description": (
            "Capability state aggregated to STANDBY because "
            "the Dish Manager's dish mode is STANDBY_sLP or STANDBY_FP, "
            "the SPF capability state is STANDBY, "
            "OPERATE_DEGRADED, or OPERATE_FULL, and "
            "the SPFRX capability state is STANDBY or OPERATE."
        ),
    },

    "STANDBY_2": {
        "rule": rule_engine.Rule(
            "("
            "DM.dishmode == 'DishMode.STOW' "
            "and "
            "DS.indexerposition != 'IndexerPosition.MOVING'"
            ") "
            "and "
            "SPF.capabilitystate == 'SPFCapabilityStates.STANDBY' "
            "and "
            "SPFRX.capabilitystate in "
            "['SPFRxCapabilityStates.STANDBY', "
            "'SPFRxCapabilityStates.OPERATE']"
        ),
        "description": (
            "Capability state aggregated to STANDBY because "
            "the Dish Manager's dish mode is STOW, "
            "the Dish Structure's indexer position is not MOVING, "
            "the SPF capability state is STANDBY, and "
            "the SPFRX capability state is STANDBY or OPERATE."
        ),
    },

    "STANDBY_3": {
        "rule": rule_engine.Rule(
            "DM.dishmode == 'DishMode.MAINTENANCE' "
            "and "
            "SPF.capabilitystate in "
            "['SPFCapabilityStates.STANDBY', "
            "'SPFCapabilityStates.OPERATE_DEGRADED', "
            "'SPFCapabilityStates.OPERATE_FULL'] "
            "and "
            "SPFRX.capabilitystate == "
            "'SPFRxCapabilityStates.STANDBY'"
        ),
        "description": (
            "Capability state aggregated to STANDBY because "
            "the Dish Manager's dish mode is MAINTENANCE, "
            "the SPF capability state is STANDBY, "
            "OPERATE_DEGRADED, or OPERATE_FULL, and "
            "the SPFRX capability state is STANDBY."
        ),
    },

    "OPERATE_FULL": {
        "rule": rule_engine.Rule(
            "DM.dishmode in "
            "['DishMode.STOW', 'DishMode.OPERATE'] "
            "and "
            "SPF.capabilitystate == "
            "'SPFCapabilityStates.OPERATE_FULL' "
            "and "
            "SPFRX.capabilitystate == "
            "'SPFRxCapabilityStates.OPERATE'"
        ),
        "description": (
            "Capability state aggregated to OPERATE_FULL because "
            "the Dish Manager's dish mode is STOW or OPERATE, "
            "the SPF capability state is OPERATE_FULL, and "
            "the SPFRX capability state is OPERATE."
        ),
    },

    "CONFIGURING": {
        "rule": rule_engine.Rule(
            "DM.dishmode == 'DishMode.CONFIG' "
            "and "
            "SPF.capabilitystate in "
            "['SPFCapabilityStates.OPERATE_DEGRADED', "
            "'SPFCapabilityStates.OPERATE_FULL'] "
            "and "
            "SPFRX.capabilitystate in "
            "['SPFRxCapabilityStates.CONFIGURE', "
            "'SPFRxCapabilityStates.OPERATE']"
        ),
        "description": (
            "Capability state aggregated to CONFIGURING because "
            "the Dish Manager's dish mode is CONFIG, "
            "the SPF capability state is OPERATE_DEGRADED or OPERATE_FULL, "
            "and the SPFRX capability state is CONFIGURE or OPERATE."
        ),
    },

    "OPERATE_DEGRADED": {
        "rule": rule_engine.Rule(
            "("
            "DS.indexerposition != 'IndexerPosition.MOVING' "
            "and "
            "DS.operatingmode in "
            "['DSOperatingMode.STOW', "
            "'DSOperatingMode.POINT']"
            ") "
            "and "
            "SPF.capabilitystate == "
            "'SPFCapabilityStates.OPERATE_DEGRADED' "
            "and "
            "SPFRX.capabilitystate == "
            "'SPFRxCapabilityStates.OPERATE'"
        ),
        "description": (
            "Capability state aggregated to OPERATE_DEGRADED because "
            "the Dish Structure's indexer position is not MOVING, "
            "the Dish Structure's operating mode is STOW or POINT, "
            "the SPF capability state is OPERATE_DEGRADED, and "
            "the SPFRX capability state is OPERATE."
        ),
    },
}


CAPABILITY_STATE_RULES_SPF_IGNORED = {
    "UNAVAILABLE": {
        "rule": rule_engine.Rule(
            "(DS.operatingmode == 'DSOperatingMode.STARTUP' or "
            "DS.operatingmode == 'DSOperatingMode.ESTOP') "
            "and "
            "SPFRX.capabilitystate == "
            "'SPFRxCapabilityStates.UNAVAILABLE'"
        ),
        "description": (
            "Capability state aggregated to UNAVAILABLE because "
            "the Dish Structure's operating mode is STARTUP or ESTOP, "
            "the SPFRX capability state is UNAVAILABLE, and "
            "SPF inputs are ignored."
        ),
    },

    "STANDBY_1": {
        "rule": rule_engine.Rule(
            "DM.dishmode in "
            "['DishMode.STANDBY_LP', 'DishMode.STANDBY_FP'] "
            "and "
            "SPFRX.capabilitystate in "
            "['SPFRxCapabilityStates.STANDBY', "
            "'SPFRxCapabilityStates.OPERATE']"
        ),
        "description": (
            "Capability state aggregated to STANDBY because "
            "the Dish Manager's dish mode is STANDBY_LP or STANDBY_FP, "
            "the SPFRX capability state is STANDBY or OPERATE, "
            "and SPF inputs are ignored."
        ),
    },

    "STANDBY_2": {
        "rule": rule_engine.Rule(
            "("
            "DM.dishmode == 'DishMode.STOW' "
            "and "
            "DS.indexerposition != 'IndexerPosition.MOVING'"
            ") "
            "and "
            "SPFRX.capabilitystate in "
            "['SPFRxCapabilityStates.STANDBY', "
            "'SPFRxCapabilityStates.OPERATE']"
        ),
        "description": (
            "Capability state aggregated to STANDBY because "
            "the Dish Manager's dish mode is STOW, "
            "the Dish Structure's indexer position is not MOVING, "
            "the SPFRX capability state is STANDBY or OPERATE, "
            "and SPF inputs are ignored."
        ),
    },

    "STANDBY_3": {
        "rule": rule_engine.Rule(
            "DM.dishmode == 'DishMode.MAINTENANCE' "
            "and "
            "SPFRX.capabilitystate == "
            "'SPFRxCapabilityStates.STANDBY'"
        ),
        "description": (
            "Capability state aggregated to STANDBY because "
            "the Dish Manager's dish mode is MAINTENANCE, "
            "the SPFRX capability state is STANDBY, and "
            "SPF inputs are ignored."
        ),
    },

    "OPERATE_FULL": {
        "rule": rule_engine.Rule(
            "DM.dishmode in "
            "['DishMode.STOW', 'DishMode.OPERATE'] "
            "and "
            "SPFRX.capabilitystate == "
            "'SPFRxCapabilityStates.OPERATE'"
        ),
        "description": (
            "Capability state aggregated to OPERATE_FULL because "
            "the Dish Manager's dish mode is STOW or OPERATE, "
            "the SPFRX capability state is OPERATE, and "
            "SPF inputs are ignored."
        ),
    },

    "CONFIGURING": {
        "rule": rule_engine.Rule(
            "DM.dishmode == 'DishMode.CONFIG' "
            "and "
            "SPFRX.capabilitystate in "
            "['SPFRxCapabilityStates.CONFIGURE', "
            "'SPFRxCapabilityStates.OPERATE']"
        ),
        "description": (
            "Capability state aggregated to CONFIGURING because "
            "the Dish Manager's dish mode is CONFIG, "
            "the SPFRX capability state is CONFIGURE or OPERATE, "
            "and SPF inputs are ignored."
        ),
    },

    "OPERATE_DEGRADED": {
        "rule": rule_engine.Rule(
            "("
            "DS.indexerposition != 'IndexerPosition.MOVING' "
            "and "
            "DS.operatingmode in "
            "['DSOperatingMode.STOW', "
            "'DSOperatingMode.POINT']"
            ") "
            "and "
            "SPFRX.capabilitystate == "
            "'SPFRxCapabilityStates.OPERATE'"
        ),
        "description": (
            "Capability state aggregated to OPERATE_DEGRADED because "
            "the Dish Structure's indexer position is not MOVING, "
            "the Dish Structure's operating mode is STOW or POINT, "
            "the SPFRX capability state is OPERATE, and "
            "SPF inputs are ignored."
        ),
    },
}


CAPABILITY_STATE_RULES_SPFRX_IGNORED = {
    "UNAVAILABLE": {
        "rule": rule_engine.Rule(
            "(DS.operatingmode == 'DSOperatingMode.STARTUP' or "
            "DS.operatingmode == 'DSOperatingMode.ESTOP') "
            "and "
            "SPF.capabilitystate == "
            "'SPFCapabilityStates.UNAVAILABLE'"
        ),
        "description": (
            "Capability state aggregated to UNAVAILABLE because "
            "the Dish Structure's operating mode is STARTUP or ESTOP, "
            "the SPF capability state is UNAVAILABLE, and "
            "SPFRX inputs are ignored."
        ),
    },

    "STANDBY_1": {
        "rule": rule_engine.Rule(
            "DM.dishmode in "
            "['DishMode.STANDBY_LP', 'DishMode.STANDBY_FP'] "
            "and "
            "SPF.capabilitystate in "
            "['SPFCapabilityStates.STANDBY', "
            "'SPFCapabilityStates.OPERATE_DEGRADED', "
            "'SPFCapabilityStates.OPERATE_FULL']"
        ),
        "description": (
            "Capability state aggregated to STANDBY because "
            "the Dish Manager's dish mode is STANDBY_LP or STANDBY_FP, "
            "the SPF capability state is STANDBY, "
            "OPERATE_DEGRADED, or OPERATE_FULL, and "
            "SPFRX inputs are ignored."
        ),
    },

    "STANDBY_2": {
        "rule": rule_engine.Rule(
            "("
            "DM.dishmode == 'DishMode.STOW' "
            "and "
            "DS.indexerposition != 'IndexerPosition.MOVING'"
            ") "
            "and "
            "SPF.capabilitystate == "
            "'SPFCapabilityStates.STANDBY'"
        ),
        "description": (
            "Capability state aggregated to STANDBY because "
            "the Dish Manager's dish mode is STOW, "
            "the Dish Structure's indexer position is not MOVING, "
            "the SPF capability state is STANDBY, and "
            "SPFRX inputs are ignored."
        ),
    },

    "STANDBY_3": {
        "rule": rule_engine.Rule(
            "DM.dishmode == 'DishMode.MAINTENANCE' "
            "and "
            "SPF.capabilitystate in "
            "['SPFCapabilityStates.STANDBY', "
            "'SPFCapabilityStates.OPERATE_DEGRADED', "
            "'SPFCapabilityStates.OPERATE_FULL']"
        ),
        "description": (
            "Capability state aggregated to STANDBY because "
            "the Dish Manager's dish mode is MAINTENANCE, "
            "the SPF capability state is STANDBY, "
            "OPERATE_DEGRADED, or OPERATE_FULL, and "
            "SPFRX inputs are ignored."
        ),
    },

    "OPERATE_FULL": {
        "rule": rule_engine.Rule(
            "DM.dishmode in "
            "['DishMode.STOW', 'DishMode.OPERATE'] "
            "and "
            "SPF.capabilitystate == "
            "'SPFCapabilityStates.OPERATE_FULL'"
        ),
        "description": (
            "Capability state aggregated to OPERATE_FULL because "
            "the Dish Manager's dish mode is STOW or OPERATE, "
            "the SPF capability state is OPERATE_FULL, and "
            "SPFRX inputs are ignored."
        ),
    },

    "CONFIGURING": {
        "rule": rule_engine.Rule(
            "DM.dishmode == 'DishMode.CONFIG' "
            "and "
            "SPF.capabilitystate in "
            "['SPFCapabilityStates.OPERATE_DEGRADED', "
            "'SPFCapabilityStates.OPERATE_FULL']"
        ),
        "description": (
            "Capability state aggregated to CONFIGURING because "
            "the Dish Manager's dish mode is CONFIG, "
            "the SPF capability state is OPERATE_DEGRADED or OPERATE_FULL, "
            "and SPFRX inputs are ignored."
        ),
    },

    "OPERATE_DEGRADED": {
        "rule": rule_engine.Rule(
            "("
            "DS.indexerposition != 'IndexerPosition.MOVING' "
            "and "
            "DS.operatingmode in "
            "['DSOperatingMode.STOW', "
            "'DSOperatingMode.POINT']"
            ") "
            "and "
            "SPF.capabilitystate == "
            "'SPFCapabilityStates.OPERATE_DEGRADED'"
        ),
        "description": (
            "Capability state aggregated to OPERATE_DEGRADED because "
            "the Dish Structure's indexer position is not MOVING, "
            "the Dish Structure's operating mode is STOW or POINT, "
            "the SPF capability state is OPERATE_DEGRADED, and "
            "SPFRX inputs are ignored."
        ),
    },
}


CAPABILITY_STATE_RULES_DS_ONLY = {
    "UNAVAILABLE": {
        "rule": rule_engine.Rule(
            "(DS.operatingmode == 'DSOperatingMode.STARTUP' or "
            "DS.operatingmode == 'DSOperatingMode.ESTOP')"
        ),
        "description": (
            "Capability state aggregated to UNAVAILABLE because "
            "the Dish Structure's operating mode is STARTUP or ESTOP, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "STANDBY_1": {
        "rule": rule_engine.Rule(
            "DM.dishmode in "
            "['DishMode.STANDBY_LP', 'DishMode.STANDBY_FP']"
        ),
        "description": (
            "Capability state aggregated to STANDBY because "
            "the Dish Manager's dish mode is STANDBY_LP or STANDBY_FP, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "STANDBY_2": {
        "rule": rule_engine.Rule(
            "("
            "DM.dishmode == 'DishMode.STOW' "
            "and "
            "DS.indexerposition != 'IndexerPosition.MOVING'"
            ")"
        ),
        "description": (
            "Capability state aggregated to STANDBY because "
            "the Dish Manager's dish mode is STOW, "
            "the Dish Structure's indexer position is not MOVING, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "STANDBY_3": {
        "rule": rule_engine.Rule(
            "DM.dishmode == 'DishMode.MAINTENANCE'"
        ),
        "description": (
            "Capability state aggregated to STANDBY because "
            "the Dish Manager's dish mode is MAINTENANCE, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "OPERATE_FULL": {
        "rule": rule_engine.Rule(
            "DM.dishmode in "
            "['DishMode.STOW', 'DishMode.OPERATE']"
        ),
        "description": (
            "Capability state aggregated to OPERATE_FULL because "
            "the Dish Manager's dish mode is STOW or OPERATE, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "CONFIGURING": {
        "rule": rule_engine.Rule(
            "DM.dishmode == 'DishMode.CONFIG'"
        ),
        "description": (
            "Capability state aggregated to CONFIGURING because "
            "the Dish Manager's dish mode is CONFIG, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "OPERATE_DEGRADED": {
        "rule": rule_engine.Rule(
            "("
            "DS.indexerposition != 'IndexerPosition.MOVING' "
            "and "
            "DS.operatingmode in "
            "['DSOperatingMode.STOW', "
            "'DSOperatingMode.POINT']"
            ")"
        ),
        "description": (
            "Capability state aggregated to OPERATE_DEGRADED because "
            "the Dish Structure's indexer position is not MOVING, "
            "the Dish Structure's operating mode is STOW or POINT, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },
}