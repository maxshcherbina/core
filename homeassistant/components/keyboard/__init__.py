"""Support to emulate keyboard presses on host machine."""

from pykeyboard import PyKeyboard
import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    SERVICE_MEDIA_NEXT_TRACK,
    SERVICE_MEDIA_PLAY_PAUSE,
    SERVICE_MEDIA_PREVIOUS_TRACK,
    SERVICE_VOLUME_DOWN,
    SERVICE_VOLUME_MUTE,
    SERVICE_VOLUME_UP,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

DOMAIN = "keyboard"

TAP_KEY_SCHEMA = vol.Schema({})

CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Keyboard from a config entry."""
    return await async_setup(hass, dict(entry.data))


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Listen for keyboard events."""
    keyboard = PyKeyboard()
    keyboard.special_key_assignment()

    hass.services.register(
        DOMAIN,
        SERVICE_VOLUME_UP,
        lambda service: keyboard.tap_key(keyboard.volume_up_key),
        schema=TAP_KEY_SCHEMA,
    )

    hass.services.register(
        DOMAIN,
        SERVICE_VOLUME_DOWN,
        lambda service: keyboard.tap_key(keyboard.volume_down_key),
        schema=TAP_KEY_SCHEMA,
    )

    hass.services.register(
        DOMAIN,
        SERVICE_VOLUME_MUTE,
        lambda service: keyboard.tap_key(keyboard.volume_mute_key),
        schema=TAP_KEY_SCHEMA,
    )

    hass.services.register(
        DOMAIN,
        SERVICE_MEDIA_PLAY_PAUSE,
        lambda service: keyboard.tap_key(keyboard.media_play_pause_key),
        schema=TAP_KEY_SCHEMA,
    )

    hass.services.register(
        DOMAIN,
        SERVICE_MEDIA_NEXT_TRACK,
        lambda service: keyboard.tap_key(keyboard.media_next_track_key),
        schema=TAP_KEY_SCHEMA,
    )

    hass.services.register(
        DOMAIN,
        SERVICE_MEDIA_PREVIOUS_TRACK,
        lambda service: keyboard.tap_key(keyboard.media_prev_track_key),
        schema=TAP_KEY_SCHEMA,
    )
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    # Unregister services associated with the domain
    for service in (
        SERVICE_VOLUME_UP,
        SERVICE_VOLUME_DOWN,
        SERVICE_VOLUME_MUTE,
        SERVICE_MEDIA_PLAY_PAUSE,
        SERVICE_MEDIA_NEXT_TRACK,
        SERVICE_MEDIA_PREVIOUS_TRACK,
    ):
        hass.services.async_remove(DOMAIN, service)

    return await hass.config_entries.async_unload_platforms(entry, [])


# def setup(hass: HomeAssistant, config: ConfigType) -> bool:
#     """Listen for keyboard events."""

# keyboard = PyKeyboard()
# keyboard.special_key_assignment()

# hass.services.register(
#     DOMAIN,
#     SERVICE_VOLUME_UP,
#     lambda service: keyboard.tap_key(keyboard.volume_up_key),
#     schema=TAP_KEY_SCHEMA,
# )

# hass.services.register(
#     DOMAIN,
#     SERVICE_VOLUME_DOWN,
#     lambda service: keyboard.tap_key(keyboard.volume_down_key),
#     schema=TAP_KEY_SCHEMA,
# )

# hass.services.register(
#     DOMAIN,
#     SERVICE_VOLUME_MUTE,
#     lambda service: keyboard.tap_key(keyboard.volume_mute_key),
#     schema=TAP_KEY_SCHEMA,
# )

# hass.services.register(
#     DOMAIN,
#     SERVICE_MEDIA_PLAY_PAUSE,
#     lambda service: keyboard.tap_key(keyboard.media_play_pause_key),
#     schema=TAP_KEY_SCHEMA,
# )

# hass.services.register(
#     DOMAIN,
#     SERVICE_MEDIA_NEXT_TRACK,
#     lambda service: keyboard.tap_key(keyboard.media_next_track_key),
#     schema=TAP_KEY_SCHEMA,
# )

# hass.services.register(
#     DOMAIN,
#     SERVICE_MEDIA_PREVIOUS_TRACK,
#     lambda service: keyboard.tap_key(keyboard.media_prev_track_key),
#     schema=TAP_KEY_SCHEMA,
# )
# return True
