"""Advice for achieving power states."""

from app.models.enums import PowerState


POWER_STATE_ADVICE_ALL_DEVICES = {
    PowerState.UPS: (
        "The Dish Structure power state must be UPS or OFF."
    ),

    PowerState.LOW: (
        (
            "The Dish Structure power state must be LOW_POWER, or if its "
            "power state is UNKNOWN, the SPF power state must be LOW_POWER."
        ),
        (
            "The Dish Structure power state must be UNKNOWN and the SPF "
            "power state must be LOW_POWER."
        ),
        (
            "Both the Dish Structure and SPF power states must be UNKNOWN."
        ),
    ),

    PowerState.FULL: (
        (
            "The Dish Structure power state must be FULL_POWER, or if its "
            "power state is UNKNOWN, the SPF power state must be FULL_POWER."
        ),
        (
            "The Dish Structure power state must be UNKNOWN and the SPF "
            "power state must be FULL_POWER."
        ),
    ),
}


POWER_STATE_ADVICE_SPF_IGNORED = {
    PowerState.UPS: (
        "The Dish Structure power state must be UPS or OFF."
    ),

    PowerState.LOW: (
        "The Dish Structure power state must be LOW_POWER or UNKNOWN."
    ),

    PowerState.FULL: (
        "The Dish Structure power state must be FULL_POWER."
    ),
}


POWER_STATE_ADVICE_DS_ONLY = {
    PowerState.UPS: (
        "The Dish Structure power state must be UPS or OFF."
    ),

    PowerState.LOW: (
        "The Dish Structure power state must be LOW_POWER or UNKNOWN."
    ),

    PowerState.FULL: (
        "The Dish Structure power state must be FULL_POWER."
    ),
}


def get_power_state_advice(
    power_state: PowerState,
) -> tuple:
    """Return advice for achieving the requested power state."""

    return (
        POWER_STATE_ADVICE_ALL_DEVICES[power_state],
        POWER_STATE_ADVICE_SPF_IGNORED[power_state],
        [],
        POWER_STATE_ADVICE_DS_ONLY[power_state],
    )