"""Config flow for the Keyboard integration."""

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.config_entries import ConfigFlowResult

from .const import DOMAIN  # type: ignore[import-not-found]


class KeyboardConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for the Keyboard integration."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(self, user_input=None) -> config_entries.ConfigFlowResult:
        """Handle the initial step."""
        if user_input is not None:
            # Create a config entry if the user submits input
            return self.async_create_entry(title="Keyboard", data=user_input)

        # Define the configuration schema
        return self.async_show_form(step_id="user", data_schema=vol.Schema({}))


class KeyboardOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for the Keyboard integration."""

    def __init__(self, config_entry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None) -> ConfigFlowResult:
        """Manage the options."""
        if user_input is not None:
            # Update the configuration entry with new options
            return self.async_create_entry(title="", data=user_input)

        # Show the options form
        return self.async_show_form(step_id="init", data_schema=vol.Schema({}))
