"""Advice for achieving health states."""

from app.models.enums import HealthState


HEALTH_STATE_ADVICE_ALL_DEVICES = {
    HealthState.DEGRADED: (
        "At least one of the following must have a DEGRADED health state: "
        "Dish Structure, SPF, or SPFRX, while none of the components "
        "have a FAILED health state."
    ),

    HealthState.FAILED: (
        "At least one of the following must have a FAILED health state: "
        "Dish Structure, SPF, or SPFRX."
    ),

    HealthState.OK: (
        "The Dish Structure health state must be OK, "
        "the SPF health state must be NORMAL, "
        "and the SPFRX health state must be OK."
    ),

    HealthState.UNKNOWN: (
        "At least one of the following must have an UNKNOWN health state: "
        "Dish Structure, SPF, or SPFRX."
    ),
}


HEALTH_STATE_ADVICE_SPF_IGNORED = {
    HealthState.DEGRADED: (
        "The Dish Structure or SPFRX must have a DEGRADED health state, "
        "while neither component has a FAILED health state."
    ),

    HealthState.FAILED: (
        "The Dish Structure or SPFRX must have a FAILED health state."
    ),

    HealthState.OK: (
        "The Dish Structure and SPFRX health states must both be OK."
    ),

    HealthState.UNKNOWN: (
        "The Dish Structure or SPFRX must have an UNKNOWN health state."
    ),
}


HEALTH_STATE_ADVICE_SPFRX_IGNORED = {
    HealthState.DEGRADED: (
        "The Dish Structure or SPF must have a DEGRADED health state, "
        "while neither component has a FAILED health state."
    ),

    HealthState.FAILED: (
        "The Dish Structure or SPF must have a FAILED health state."
    ),

    HealthState.OK: (
        "The Dish Structure health state must be OK and "
        "the SPF health state must be NORMAL."
    ),

    HealthState.UNKNOWN: (
        "The Dish Structure or SPF must have an UNKNOWN health state."
    ),
}


HEALTH_STATE_ADVICE_DS_ONLY = {
    HealthState.DEGRADED: (
        "The Dish Structure health state must be DEGRADED."
    ),

    HealthState.FAILED: (
        "The Dish Structure health state must be FAILED."
    ),

    HealthState.OK: (
        "The Dish Structure health state must be OK."
    ),

    HealthState.UNKNOWN: (
        "The Dish Structure health state must be UNKNOWN."
    ),
}


def get_health_state_advice(
    state: HealthState,
) -> tuple:
    """Return advice for achieving the requested health state."""

    return (
        HEALTH_STATE_ADVICE_ALL_DEVICES[state],
        HEALTH_STATE_ADVICE_SPF_IGNORED[state],
        HEALTH_STATE_ADVICE_SPFRX_IGNORED[state],
        HEALTH_STATE_ADVICE_DS_ONLY[state],
    )