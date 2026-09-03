"""Advice for achieving dish modes."""

from app.models.enums import DishMode


DISH_MODE_ADVICE_ALL_DEVICES = {
    DishMode.STARTUP: (
        "At least one of the following must be in STARTUP: "
        "Dish Structure, SPF, or SPFRX."
    ),

    DishMode.STOW: (
        "The Dish Structure operating mode must be STOW."
    ),

    DishMode.CONFIG: (
        "The SPFRX operating mode must be CONFIGURE, "
        "or the Dish Structure indexer position must be MOVING."
    ),

    DishMode.OPERATE: (
        "The Dish Structure operating mode must be POINT, "
        "the SPF operating mode must be OPERATE, "
        "and the SPFRX operating mode must be OPERATE."
    ),

    DishMode.STANDBY_LP: (
        "The Dish Structure operating mode must be STANDBY, "
        "its power state must be LOW_POWER, "
        "and the SPF operating mode must not be OPERATE."
    ),

    DishMode.STANDBY_FP: (
        "The Dish Structure operating mode must be STANDBY "
        "and its power state must be FULL_POWER."
    ),
}


DISH_MODE_ADVICE_SPF_IGNORED = {
    DishMode.STARTUP: (
        "At least one of the following must be in STARTUP: "
        "Dish Structure or SPFRX."
    ),

    DishMode.STOW: (
        "The Dish Structure operating mode must be STOW."
    ),

    DishMode.CONFIG: (
        "The SPFRX operating mode must be CONFIGURE, "
        "or the Dish Structure indexer position must be MOVING."
    ),

    DishMode.OPERATE: (
        "The Dish Structure operating mode must be POINT "
        "and the SPFRX operating mode must be OPERATE."
    ),

    DishMode.STANDBY_LP: (
        "The Dish Structure operating mode must be STANDBY "
        "and its power state must be LOW_POWER."
    ),

    DishMode.STANDBY_FP: (
        "The Dish Structure operating mode must be STANDBY "
        "and its power state must be FULL_POWER."
    ),
}


DISH_MODE_ADVICE_SPFRX_IGNORED = {
    DishMode.STARTUP: (
        "At least one of the following must be in STARTUP: "
        "Dish Structure or SPF."
    ),

    DishMode.STOW: (
        "The Dish Structure operating mode must be STOW."
    ),

    DishMode.CONFIG: (
        "The Dish Structure indexer position must be MOVING."
    ),

    DishMode.OPERATE: (
        "The Dish Structure operating mode must be POINT "
        "and the SPF operating mode must be OPERATE."
    ),

    DishMode.STANDBY_LP: (
        "The Dish Structure operating mode must be STANDBY, "
        "its power state must be LOW_POWER, "
        "and the SPF operating mode must not be OPERATE."
    ),

    DishMode.STANDBY_FP: (
        "The Dish Structure operating mode must be STANDBY "
        "and its power state must be FULL_POWER."
    ),
}


DISH_MODE_ADVICE_DS_ONLY = {
    DishMode.STARTUP: (
        "The Dish Structure operating mode must be STARTUP."
    ),

    DishMode.STOW: (
        "The Dish Structure operating mode must be STOW."
    ),

    DishMode.CONFIG: (
        "The Dish Structure indexer position must be MOVING."
    ),

    DishMode.OPERATE: (
        "The Dish Structure operating mode must be POINT."
    ),

    DishMode.STANDBY_LP: (
        "The Dish Structure operating mode must be STANDBY "
        "and its power state must be LOW_POWER."
    ),

    DishMode.STANDBY_FP: (
        "The Dish Structure operating mode must be STANDBY "
        "and its power state must be FULL_POWER."
    ),
}


def get_dish_mode_advice(
    mode: DishMode,
) -> tuple:
    """Return advice for achieving the requested dish mode."""

    return (
        DISH_MODE_ADVICE_ALL_DEVICES[mode],
        DISH_MODE_ADVICE_SPF_IGNORED[mode],
        DISH_MODE_ADVICE_SPFRX_IGNORED[mode],
        DISH_MODE_ADVICE_DS_ONLY[mode],
    )