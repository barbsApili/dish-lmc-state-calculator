"""Advice for achieving configured bands."""

from app.models.enums import Band


CONFIGURED_BAND_ADVICE_ALL_DEVICES = {
    Band.NONE: (
        "The SPFRX configured band must be NONE."
    ),

    Band.B1: (
        "The Dish Structure indexer position must be B1, "
        "the SPFRX configured band must be B1, "
        "and the SPF band in focus must be B1."
    ),

    Band.B2: (
        "The Dish Structure indexer position must be B2, "
        "the SPFRX configured band must be B2, "
        "and the SPF band in focus must be B2."
    ),

    Band.B3: (
        "The Dish Structure indexer position must be B3, "
        "the SPFRX configured band must be B3, "
        "and the SPF band in focus must be B3."
    ),

    Band.B4: (
        "The Dish Structure indexer position must be B4, "
        "the SPFRX configured band must be B4, "
        "and the SPF band in focus must be B4."
    ),

    Band.B5a: (
        "The Dish Structure indexer position must be B5a, "
        "the SPFRX configured band must be B5a, "
        "and the SPF band in focus must be B5a."
    ),

    Band.B5b: (
        "The Dish Structure indexer position must be B5b, "
        "the SPFRX configured band must be B1, "
        "and the SPF band in focus must be B5b."
    ),
}


CONFIGURED_BAND_ADVICE_SPF_IGNORED = {
    Band.NONE: (
        "The SPFRX configured band must be NONE."
    ),

    Band.B1: (
        "The Dish Structure indexer position must be B1 "
        "and the SPFRX configured band must be B1."
    ),

    Band.B2: (
        "The Dish Structure indexer position must be B2 "
        "and the SPFRX configured band must be B2."
    ),

    Band.B3: (
        "The Dish Structure indexer position must be B3 "
        "and the SPFRX configured band must be B3."
    ),

    Band.B4: (
        "The Dish Structure indexer position must be B4 "
        "and the SPFRX configured band must be B4."
    ),

    Band.B5a: (
        "The Dish Structure indexer position must be B5a "
        "and the SPFRX configured band must be B5a."
    ),

    Band.B5b: (
        "The Dish Structure indexer position must be B5b "
        "and the SPFRX configured band must be B1."
    ),
}


CONFIGURED_BAND_ADVICE_SPFRX_IGNORED = {
    Band.B1: (
        "The Dish Structure indexer position must be B1 "
        "and the SPF band in focus must be B1."
    ),

    Band.B2: (
        "The Dish Structure indexer position must be B2 "
        "and the SPF band in focus must be B2."
    ),

    Band.B3: (
        "The Dish Structure indexer position must be B3 "
        "and the SPF band in focus must be B3."
    ),

    Band.B4: (
        "The Dish Structure indexer position must be B4 "
        "and the SPF band in focus must be B4."
    ),

    Band.B5a: (
        "The Dish Structure indexer position must be B5a "
        "and the SPF band in focus must be B5a."
    ),

    Band.B5b: (
        "The Dish Structure indexer position must be B5b "
        "and the SPF band in focus must be B5b."
    ),
}


CONFIGURED_BAND_ADVICE_DS_ONLY = {
    Band.B1: (
        "The Dish Structure indexer position must be B1."
    ),

    Band.B2: (
        "The Dish Structure indexer position must be B2."
    ),

    Band.B3: (
        "The Dish Structure indexer position must be B3."
    ),

    Band.B4: (
        "The Dish Structure indexer position must be B4."
    ),

    Band.B5a: (
        "The Dish Structure indexer position must be B5a."
    ),

    Band.B5b: (
        "The Dish Structure indexer position must be B5b."
    ),
}


def get_configured_band_advice(
    band: Band,
) -> tuple:
    """Return advice for achieving the requested configured band."""

    return (
        CONFIGURED_BAND_ADVICE_ALL_DEVICES[band],
        CONFIGURED_BAND_ADVICE_SPF_IGNORED[band],
        CONFIGURED_BAND_ADVICE_SPFRX_IGNORED[band],
        CONFIGURED_BAND_ADVICE_DS_ONLY[band],
    )