"""Automatic transition rules for configuredBand."""

import rule_engine


CONFIGURED_BAND_RULES_ALL_DEVICES = {
    "NONE": {
        "rule": rule_engine.Rule(
            "SPFRX.configuredband == 'Band.NONE'"
        ),
        "description": (
            "Configured band aggregated to NONE because "
            "the SPFRX configured band is NONE."
        ),
    },

    "B1": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B1' and "
            "SPFRX.configuredband == 'Band.B1' and "
            "SPF.bandinfocus == 'SPFBandInFocus.B1'"
        ),
        "description": (
            "Configured band aggregated to B1 because "
            "the Dish Structure's indexer position is B1, "
            "the SPFRX configured band is B1, and "
            "the SPF band in focus is B1."
        ),
    },

    "B2": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B2' and "
            "SPFRX.configuredband == 'Band.B2' and "
            "SPF.bandinfocus == 'SPFBandInFocus.B2'"
        ),
        "description": (
            "Configured band aggregated to B2 because "
            "the Dish Structure's indexer position is B2, "
            "the SPFRX configured band is B2, and "
            "the SPF band in focus is B2."
        ),
    },

    "B3": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B3' and "
            "SPFRX.configuredband == 'Band.B3' and "
            "SPF.bandinfocus == 'SPFBandInFocus.B3'"
        ),
        "description": (
            "Configured band aggregated to B3 because "
            "the Dish Structure's indexer position is B3, "
            "the SPFRX configured band is B3, and "
            "the SPF band in focus is B3."
        ),
    },

    "B4": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B4' and "
            "SPFRX.configuredband == 'Band.B4' and "
            "SPF.bandinfocus == 'SPFBandInFocus.B4'"
        ),
        "description": (
            "Configured band aggregated to B4 because "
            "the Dish Structure's indexer position is B4, "
            "the SPFRX configured band is B4, and "
            "the SPF band in focus is B4."
        ),
    },

    "B5a": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B5a' and "
            "SPFRX.configuredband == 'Band.B5a' and "
            "SPF.bandinfocus == 'SPFBandInFocus.B5a'"
        ),
        "description": (
            "Configured band aggregated to B5a because "
            "the Dish Structure's indexer position is B5a, "
            "the SPFRX configured band is B5a, and "
            "the SPF band in focus is B5a."
        ),
    },

    "B5b": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B5b' and "
            "SPFRX.configuredband == 'Band.B1' and "
            "SPF.bandinfocus == 'SPFBandInFocus.B5b'"
        ),
        "description": (
            "Configured band aggregated to B5b because "
            "the Dish Structure's indexer position is B5b, "
            "the SPF band in focus is B5b, and "
            "the SPFRX configured band is Band.B1 as "
            "the expected receiver mapping for the "
            "B5b hardware configuration."
        ),
    },
}


CONFIGURED_BAND_RULES_SPF_IGNORED = {
    "NONE": {
        "rule": rule_engine.Rule(
            "SPFRX.configuredband == 'Band.NONE'"
        ),
        "description": (
            "Configured band aggregated to NONE because "
            "the SPFRX configured band is NONE and "
            "SPF inputs are ignored."
        ),
    },

    "B1": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B1' and "
            "SPFRX.configuredband == 'Band.B1'"
        ),
        "description": (
            "Configured band aggregated to B1 because "
            "the Dish Structure's indexer position is B1, "
            "the SPFRX configured band is B1, and "
            "SPF inputs are ignored."
        ),
    },

    "B2": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B2' and "
            "SPFRX.configuredband == 'Band.B2'"
        ),
        "description": (
            "Configured band aggregated to B2 because "
            "the Dish Structure's indexer position is B2, "
            "the SPFRX configured band is B2, and "
            "SPF inputs are ignored."
        ),
    },

    "B3": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B3' and "
            "SPFRX.configuredband == 'Band.B3'"
        ),
        "description": (
            "Configured band aggregated to B3 because "
            "the Dish Structure's indexer position is B3, "
            "the SPFRX configured band is B3, and "
            "SPF inputs are ignored."
        ),
    },

    "B4": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B4' and "
            "SPFRX.configuredband == 'Band.B4'"
        ),
        "description": (
            "Configured band aggregated to B4 because "
            "the Dish Structure's indexer position is B4, "
            "the SPFRX configured band is B4, and "
            "SPF inputs are ignored."
        ),
    },

    "B5a": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B5a' and "
            "SPFRX.configuredband == 'Band.B5a'"
        ),
        "description": (
            "Configured band aggregated to B5a because "
            "the Dish Structure's indexer position is B5a, "
            "the SPFRX configured band is B5a, and "
            "SPF inputs are ignored."
        ),
    },

    "B5b": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B5b' and "
            "SPFRX.configuredband == 'Band.B1'"
        ),
        "description": (
            "Configured band aggregated to B5b because "
            "the Dish Structure's indexer position is B5b, "
            "the SPFRX configured band is Band.B1 as "
            "the expected receiver mapping for the "
            "B5b hardware configuration, and "
            "SPF inputs are ignored."
        ),
    },
}


CONFIGURED_BAND_RULES_SPFRX_IGNORED = {
    "B1": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B1' and "
            "SPF.bandinfocus == 'SPFBandInFocus.B1'"
        ),
        "description": (
            "Configured band aggregated to B1 because "
            "the Dish Structure's indexer position is B1, "
            "the SPF band in focus is B1, and "
            "SPFRX inputs are ignored."
        ),
    },

    "B2": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B2' and "
            "SPF.bandinfocus == 'SPFBandInFocus.B2'"
        ),
        "description": (
            "Configured band aggregated to B2 because "
            "the Dish Structure's indexer position is B2, "
            "the SPF band in focus is B2, and "
            "SPFRX inputs are ignored."
        ),
    },

    "B3": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B3' and "
            "SPF.bandinfocus == 'SPFBandInFocus.B3'"
        ),
        "description": (
            "Configured band aggregated to B3 because "
            "the Dish Structure's indexer position is B3, "
            "the SPF band in focus is B3, and "
            "SPFRX inputs are ignored."
        ),
    },

    "B4": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B4' and "
            "SPF.bandinfocus == 'SPFBandInFocus.B4'"
        ),
        "description": (
            "Configured band aggregated to B4 because "
            "the Dish Structure's indexer position is B4, "
            "the SPF band in focus is B4, and "
            "SPFRX inputs are ignored."
        ),
    },

    "B5a": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B5a' and "
            "SPF.bandinfocus == 'SPFBandInFocus.B5a'"
        ),
        "description": (
            "Configured band aggregated to B5a because "
            "the Dish Structure's indexer position is B5a, "
            "the SPF band in focus is B5a, and "
            "SPFRX inputs are ignored."
        ),
    },

    "B5b": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B5b' and "
            "SPF.bandinfocus == 'SPFBandInFocus.B5b'"
        ),
        "description": (
            "Configured band aggregated to B5b because "
            "the Dish Structure's indexer position is B5b, "
            "the SPF band in focus is B5b, and "
            "SPFRX inputs are ignored."
        ),
    },
}


CONFIGURED_BAND_RULES_DS_ONLY = {
    "B1": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B1'"
        ),
        "description": (
            "Configured band aggregated to B1 because "
            "the Dish Structure's indexer position is B1, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "B2": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B2'"
        ),
        "description": (
            "Configured band aggregated to B2 because "
            "the Dish Structure's indexer position is B2, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "B3": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B3'"
        ),
        "description": (
            "Configured band aggregated to B3 because "
            "the Dish Structure's indexer position is B3, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "B4": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B4'"
        ),
        "description": (
            "Configured band aggregated to B4 because "
            "the Dish Structure's indexer position is B4, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "B5a": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B5a'"
        ),
        "description": (
            "Configured band aggregated to B5a because "
            "the Dish Structure's indexer position is B5a, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },

    "B5b": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B5b'"
        ),
        "description": (
            "Configured band aggregated to B5b because "
            "the Dish Structure's indexer position is B5b, "
            "and SPF and SPFRX inputs are ignored."
        ),
    },
}


SPF_BAND_IN_FOCUS_RULES_ALL_DEVICES = {
    "B1": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B1' and "
            "SPFRX.configuredband == 'Band.B1'"
        ),
        "description": (
            "SPF band in focus aggregated to B1 because "
            "the Dish Structure's indexer position is B1 "
            "and the SPFRX configured band is B1."
        ),
    },

    "B2": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B2' and "
            "SPFRX.configuredband == 'Band.B2'"
        ),
        "description": (
            "SPF band in focus aggregated to B2 because "
            "the Dish Structure's indexer position is B2 "
            "and the SPFRX configured band is B2."
        ),
    },

    "B3": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B3' and "
            "SPFRX.configuredband == 'Band.B3'"
        ),
        "description": (
            "SPF band in focus aggregated to B3 because "
            "the Dish Structure's indexer position is B3 "
            "and the SPFRX configured band is B3."
        ),
    },

    "B4": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B4' and "
            "SPFRX.configuredband == 'Band.B4'"
        ),
        "description": (
            "SPF band in focus aggregated to B4 because "
            "the Dish Structure's indexer position is B4 "
            "and the SPFRX configured band is B4."
        ),
    },

    "B5a": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B5a' and "
            "SPFRX.configuredband == 'Band.B5a'"
        ),
        "description": (
            "SPF band in focus aggregated to B5a because "
            "the Dish Structure's indexer position is B5a "
            "and the SPFRX configured band is B5a."
        ),
    },

    "B5b": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B5b' and "
            "SPFRX.configuredband == 'Band.B1'"
        ),
        "description": (
            "SPF band in focus aggregated to B5b because "
            "the Dish Structure's indexer position is B5b "
            "and the SPFRX configured band is Band.B1 "
            "for the expected B5b mapping."
        ),
    },
}


SPF_BAND_IN_FOCUS_RULES_SPFRX_IGNORED = {
    "B1": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B1'"
        ),
        "description": (
            "SPF band in focus aggregated to B1 because "
            "the Dish Structure's indexer position is B1 "
            "and SPFRX inputs are ignored."
        ),
    },

    "B2": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B2'"
        ),
        "description": (
            "SPF band in focus aggregated to B2 because "
            "the Dish Structure's indexer position is B2 "
            "and SPFRX inputs are ignored."
        ),
    },

    "B3": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B3'"
        ),
        "description": (
            "SPF band in focus aggregated to B3 because "
            "the Dish Structure's indexer position is B3 "
            "and SPFRX inputs are ignored."
        ),
    },

    "B4": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B4'"
        ),
        "description": (
            "SPF band in focus aggregated to B4 because "
            "the Dish Structure's indexer position is B4 "
            "and SPFRX inputs are ignored."
        ),
    },

    "B5a": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B5a'"
        ),
        "description": (
            "SPF band in focus aggregated to B5a because "
            "the Dish Structure's indexer position is B5a "
            "and SPFRX inputs are ignored."
        ),
    },

    "B5b": {
        "rule": rule_engine.Rule(
            "DS.indexerposition == 'IndexerPosition.B5b'"
        ),
        "description": (
            "SPF band in focus aggregated to B5b because "
            "the Dish Structure's indexer position is B5b "
            "and SPFRX inputs are ignored."
        ),
    },
}