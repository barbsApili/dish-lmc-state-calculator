# This implementation was developed with reference to the SKAO Dish LMC
# class, particularly its predefined state aggregation rules.
# The calculator is an independent implementation for analysis and
# simulation purposes (https://gitlab.com/ska-telescope/mid-dish/ska-mid-dish-manager/-/tree/main/src/ska_mid_dish_manager/models/transition_rules?ref_type=heads)

"""Automatic transition rules for dish mode."""

import rule_engine


DISH_MODE_RULES_ALL_DEVICES = {
    # MAINTENANCE mode is not aggregated from subdevices.
    # It is commanded directly on the Dish Manager.

    "STARTUP": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STARTUP' or "
            "SPF.operatingmode == 'SPFOperatingMode.STARTUP' or "
            "SPFRX.operatingmode == 'SPFRxOperatingMode.STARTUP'"
        ),
        "description": (
            "Dish mode aggregated to STARTUP because at least "
            "one subsystem's operating mode is STARTUP."
        ),
    },

    "STOW": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STOW'"
        ),
        "description": (
            "Dish mode aggregated to STOW because "
            "the Dish Structure's operating mode is STOW."
        ),
    },

    "CONFIG": {
        "rule": rule_engine.Rule(
            "SPFRX.operatingmode == "
            "'SPFRxOperatingMode.CONFIGURE' "
            "or "
            "DS.indexerposition == 'IndexerPosition.MOVING'"
        ),
        "description": (
            "Dish mode aggregated to CONFIG because "
            "the SPFRX operating mode is CONFIGURE or "
            "the Dish Structure's indexer position is MOVING."
        ),
    },

    "OPERATE": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.POINT' and "
            "SPF.operatingmode == 'SPFOperatingMode.OPERATE' and "
            "SPFRX.operatingmode == 'SPFRxOperatingMode.OPERATE'"
        ),
        "description": (
            "Dish mode aggregated to OPERATE because "
            "the Dish Structure's operating mode is POINT, "
            "the SPF operating mode is OPERATE, and "
            "the SPFRX operating mode is OPERATE."
        ),
    },

    "STANDBY_LP": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STANDBY' and "
            "DS.powerstate == 'DSPowerState.LOW_POWER' and "
            "SPF.operatingmode != 'SPFOperatingMode.OPERATE'"
        ),
        "description": (
            "Dish mode aggregated to STANDBY_LP because "
            "the Dish Structure's operating mode is STANDBY, "
            "the Dish Structure's power state is LOW_POWER, "
            "and the SPF operating mode is not OPERATE."
        ),
    },

    "STANDBY_FP": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STANDBY' and "
            "DS.powerstate == 'DSPowerState.FULL_POWER'"
        ),
        "description": (
            "Dish mode aggregated to STANDBY_FP because "
            "the Dish Structure's operating mode is STANDBY "
            "and the Dish Structure's power state is FULL_POWER."
        ),
    },
}


DISH_MODE_RULES_SPF_IGNORED = {
    "STARTUP": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STARTUP' or "
            "SPFRX.operatingmode == 'SPFRxOperatingMode.STARTUP'"
        ),
        "description": (
            "Dish mode aggregated to STARTUP because "
            "the Dish Structure's operating mode or "
            "the SPFRX operating mode is STARTUP, and "
            "SPF inputs are ignored."
        ),
    },

    "STOW": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STOW'"
        ),
        "description": (
            "Dish mode aggregated to STOW because "
            "the Dish Structure's operating mode is STOW "
            "and SPF inputs are ignored."
        ),
    },

    "CONFIG": {
        "rule": rule_engine.Rule(
            "SPFRX.operatingmode == "
            "'SPFRxOperatingMode.CONFIGURE' "
            "or "
            "DS.indexerposition == 'IndexerPosition.MOVING'"
        ),
        "description": (
            "Dish mode aggregated to CONFIG because "
            "the SPFRX operating mode is CONFIGURE or "
            "the Dish Structure's indexer position is MOVING, "
            "and SPF inputs are ignored."
        ),
    },

    "OPERATE": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.POINT' and "
            "SPFRX.operatingmode == "
            "'SPFRxOperatingMode.OPERATE'"
        ),
        "description": (
            "Dish mode aggregated to OPERATE because "
            "the Dish Structure's operating mode is POINT, "
            "the SPFRX operating mode is OPERATE, and "
            "SPF inputs are ignored."
        ),
    },

    "STANDBY_LP": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STANDBY' and "
            "DS.powerstate == 'DSPowerState.LOW_POWER'"
        ),
        "description": (
            "Dish mode aggregated to STANDBY_LP because "
            "the Dish Structure's operating mode is STANDBY, "
            "the Dish Structure's power state is LOW_POWER, "
            "and SPF inputs are ignored."
        ),
    },

    "STANDBY_FP": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STANDBY' and "
            "DS.powerstate == 'DSPowerState.FULL_POWER'"
        ),
        "description": (
            "Dish mode aggregated to STANDBY_FP because "
            "the Dish Structure's operating mode is STANDBY, "
            "the Dish Structure's power state is FULL_POWER, "
            "and SPF inputs are ignored."
        ),
    },
}


DISH_MODE_RULES_SPFRX_IGNORED = {
    "STARTUP": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STARTUP' or "
            "SPF.operatingmode == 'SPFOperatingMode.STARTUP'"
        ),
        "description": (
            "Dish mode aggregated to STARTUP because "
            "the Dish Structure's operating mode or "
            "the SPF operating mode is STARTUP, and "
            "SPFRX inputs are ignored."
        ),
    },

    "STOW": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STOW'"
        ),
        "description": (
            "Dish mode aggregated to STOW because "
            "the Dish Structure's operating mode is STOW "
            "and SPFRX inputs are ignored."
        ),
    },

    "CONFIG": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.MOVING'"
        ),
        "description": (
            "Dish mode aggregated to CONFIG because "
            "the Dish Structure's indexer position is MOVING "
            "and SPFRX inputs are ignored."
        ),
    },

    "OPERATE": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.POINT' and "
            "SPF.operatingmode == 'SPFOperatingMode.OPERATE'"
        ),
        "description": (
            "Dish mode aggregated to OPERATE because "
            "the Dish Structure's operating mode is POINT, "
            "the SPF operating mode is OPERATE, and "
            "SPFRX inputs are ignored."
        ),
    },

    "STANDBY_LP": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STANDBY' and "
            "DS.powerstate == 'DSPowerState.LOW_POWER' and "
            "SPF.operatingmode != 'SPFOperatingMode.OPERATE'"
        ),
        "description": (
            "Dish mode aggregated to STANDBY_LP because "
            "the Dish Structure's operating mode is STANDBY, "
            "the Dish Structure's power state is LOW_POWER, "
            "the SPF operating mode is not OPERATE, and "
            "SPFRX inputs are ignored."
        ),
    },

    "STANDBY_FP": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STANDBY' and "
            "DS.powerstate == 'DSPowerState.FULL_POWER'"
        ),
        "description": (
            "Dish mode aggregated to STANDBY_FP because "
            "the Dish Structure's operating mode is STANDBY, "
            "the Dish Structure's power state is FULL_POWER, "
            "and SPFRX inputs are ignored."
        ),
    },
}


DISH_MODE_RULES_DS_ONLY = {
    "STARTUP": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STARTUP'"
        ),
        "description": (
            "Dish mode aggregated to STARTUP because "
            "the Dish Structure's operating mode is STARTUP, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "STOW": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STOW'"
        ),
        "description": (
            "Dish mode aggregated to STOW because "
            "the Dish Structure's operating mode is STOW, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "CONFIG": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.MOVING'"
        ),
        "description": (
            "Dish mode aggregated to CONFIG because "
            "the Dish Structure's indexer position is MOVING, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "OPERATE": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.POINT'"
        ),
        "description": (
            "Dish mode aggregated to OPERATE because "
            "the Dish Structure's operating mode is POINT, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "STANDBY_LP": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STANDBY' and "
            "DS.powerstate == 'DSPowerState.LOW_POWER'"
        ),
        "description": (
            "Dish mode aggregated to STANDBY_LP because "
            "the Dish Structure's operating mode is STANDBY, "
            "the Dish Structure's power state is LOW_POWER, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "STANDBY_FP": {
        "rule": rule_engine.Rule(
            "DS.operatingmode == 'DSOperatingMode.STANDBY' and "
            "DS.powerstate == 'DSPowerState.FULL_POWER'"
        ),
        "description": (
            "Dish mode aggregated to STANDBY_FP because "
            "the Dish Structure's operating mode is STANDBY, "
            "the Dish Structure's power state is FULL_POWER, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },
}