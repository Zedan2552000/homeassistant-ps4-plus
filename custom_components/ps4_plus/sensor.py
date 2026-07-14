import logging
from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the PS4 Plus sensor platform."""
    async_add_entities([PS4ControllerBatterySensor(config_entry)])

class PS4ControllerBatterySensor(SensorEntity):
    """Representation of a PS4 Controller Battery Sensor."""

    def __init__(self, config_entry):
        """Initialize the sensor."""
        self._attr_name = f"PS4 Controller Battery"
        self._attr_unique_id = f"ps4_battery_{config_entry.entry_id}"
        self._attr_native_value = "Charging"
        self._attr_icon = "mdi:battery-charging"

    @property
    def native_value(self):
        """Return the state of the sensor."""
        # Mock value for architectural setup
        return self._attr_native_value
