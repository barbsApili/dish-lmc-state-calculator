"""Advice for achieving capability states."""

from app.models.enums import CapabilityStates


CAPABILITY_STATE_ADVICE_ALL_DEVICES = {
    CapabilityStates.UNAVAILABLE: (
        "The Dish Structure operating mode must be STARTUP or ESTOP, "
        "the SPF capability state must be UNAVAILABLE, "
        "and the SPFRX capability state must be UNAVAILABLE.",
    ),

    CapabilityStates.STANDBY: (
        "The Dish Manager dish mode must be STANDBY_LP or STANDBY_FP, "
        "the SPF capability state must be STANDBY, OPERATE_DEGRADED, "
        "or OPERATE_FULL, and the SPFRX capability state must be "
        "STANDBY or OPERATE.",

        "The Dish Manager dish mode must be STOW, the Dish Structure "
        "indexer position must not be MOVING, the SPF capability state "
        "must be STANDBY, and the SPFRX capability state must be "
        "STANDBY or OPERATE.",

        "The Dish Manager dish mode must be MAINTENANCE, the SPF "
        "capability state must be STANDBY, OPERATE_DEGRADED, or "
        "OPERATE_FULL, and the SPFRX capability state must be STANDBY.",
    ),

    CapabilityStates.OPERATE_FULL: (
        "The Dish Manager dish mode must be STOW or OPERATE, "
        "the SPF capability state must be OPERATE_FULL, "
        "and the SPFRX capability state must be OPERATE.",
    ),

    CapabilityStates.CONFIGURING: (
        "The Dish Manager dish mode must be CONFIG, the SPF "
        "capability state must be OPERATE_DEGRADED or OPERATE_FULL, "
        "and the SPFRX capability state must be CONFIGURE or OPERATE.",
    ),

    CapabilityStates.OPERATE_DEGRADED: (
        "The Dish Structure indexer position must not be MOVING, "
        "the Dish Structure operating mode must be STOW or POINT, "
        "the SPF capability state must be OPERATE_DEGRADED, "
        "and the SPFRX capability state must be OPERATE.",
    ),
}


CAPABILITY_STATE_ADVICE_SPFRX_IGNORED = {
    CapabilityStates.UNAVAILABLE: (
        "The Dish Structure operating mode must be STARTUP or ESTOP "
        "and the SPF capability state must be UNAVAILABLE.",
    ),

    CapabilityStates.STANDBY: (
        "The Dish Manager dish mode must be STANDBY_LP or STANDBY_FP "
        "and the SPF capability state must be STANDBY, "
        "OPERATE_DEGRADED, or OPERATE_FULL.",

        "The Dish Manager dish mode must be STOW, the Dish Structure "
        "indexer position must not be MOVING, and the SPF capability "
        "state must be STANDBY.",

        "The Dish Manager dish mode must be MAINTENANCE and the SPF "
        "capability state must be STANDBY, OPERATE_DEGRADED, "
        "or OPERATE_FULL.",
    ),

    CapabilityStates.OPERATE_FULL: (
        "The Dish Manager dish mode must be STOW or OPERATE "
        "and the SPF capability state must be OPERATE_FULL.",
    ),

    CapabilityStates.CONFIGURING: (
        "The Dish Manager dish mode must be CONFIG and the SPF "
        "capability state must be OPERATE_DEGRADED or OPERATE_FULL.",
    ),

    CapabilityStates.OPERATE_DEGRADED: (
        "The Dish Structure indexer position must not be MOVING, "
        "the Dish Structure operating mode must be STOW or POINT, "
        "and the SPF capability state must be OPERATE_DEGRADED.",
    ),
}


CAPABILITY_STATE_ADVICE_SPF_IGNORED = {
    CapabilityStates.UNAVAILABLE: (
        "The Dish Structure operating mode must be STARTUP or ESTOP "
        "and the SPFRX capability state must be UNAVAILABLE.",
    ),

    CapabilityStates.STANDBY: (
        "The Dish Manager dish mode must be STANDBY_LP or STANDBY_FP "
        "and the SPFRX capability state must be STANDBY or OPERATE.",

        "The Dish Manager dish mode must be STOW, the Dish Structure "
        "indexer position must not be MOVING, and the SPFRX capability "
        "state must be STANDBY or OPERATE.",

        "The Dish Manager dish mode must be MAINTENANCE and the SPFRX "
        "capability state must be STANDBY.",
    ),

    CapabilityStates.OPERATE_FULL: (
        "The Dish Manager dish mode must be STOW or OPERATE "
        "and the SPFRX capability state must be OPERATE.",
    ),

    CapabilityStates.CONFIGURING: (
        "The Dish Manager dish mode must be CONFIG and the SPFRX "
        "capability state must be CONFIGURE or OPERATE.",
    ),

    CapabilityStates.OPERATE_DEGRADED: (
        "The Dish Structure indexer position must not be MOVING, "
        "the Dish Structure operating mode must be STOW or POINT, "
        "and the SPFRX capability state must be OPERATE.",
    ),
}


CAPABILITY_STATE_ADVICE_DS_ONLY = {
    CapabilityStates.UNAVAILABLE: (
        "The Dish Structure operating mode must be STARTUP or ESTOP.",
    ),

    CapabilityStates.STANDBY: (
        "The Dish Manager dish mode must be STANDBY_LP or STANDBY_FP.",

        "The Dish Manager dish mode must be STOW and the Dish Structure "
        "indexer position must not be MOVING.",

        "The Dish Manager dish mode must be MAINTENANCE.",
    ),

    CapabilityStates.OPERATE_FULL: (
        "The Dish Manager dish mode must be STOW or OPERATE.",
    ),

    CapabilityStates.CONFIGURING: (
        "The Dish Manager dish mode must be CONFIG.",
    ),

    CapabilityStates.OPERATE_DEGRADED: (
        "The Dish Structure indexer position must not be MOVING "
        "and the Dish Structure operating mode must be STOW or POINT.",
    ),
}


def get_capability_state_advice(
    state: CapabilityStates,
) -> tuple:
    """Return advice for achieving the requested capability state."""

    return (
        CAPABILITY_STATE_ADVICE_ALL_DEVICES[state],
        CAPABILITY_STATE_ADVICE_SPFRX_IGNORED[state],
        CAPABILITY_STATE_ADVICE_SPF_IGNORED[state],
        CAPABILITY_STATE_ADVICE_DS_ONLY[state],
    )