"""Temperature helpers for Home Assistant."""
from future import annotations

from numbers import Number

from homeassistant.const import PRECISION_HALVES, PRECISION_TENTHS, PRECISION_WHOLE, TEMP_CELSIUS, TEMP_FAHRENHEIT, TEMP_KELVIN
from homeassistant.core import HomeAssistant
from homeassistant.util.unit_conversion import TemperatureConverter


def display_temp(
    hass: HomeAssistant, temperature: float | None, unit: str | None, precision: float
) -> float | None:
    """Convert temperature into preferred units/precision for display."""
    temperature_unit = unit
    ha_unit = hass.config.units.temperature_unit
    
    if temperature is None:
        return temperature
    
    # If the temperature is not a number this can cause issues
    # with Polymer components, so bail early there.
    if not isinstance(temperature, Number):
        raise TypeError(f"Temperature is not a number: {temperature}")
        
    temperature = TemperatureConverter.convert(temperature, ha_unit, temperature_unit)

    return round_temperature(temperature, precision)


def round_temperature(
    temperature: float, precision: float
) -> float:
    """Round in the units appropriate for the precision."""

    # convert to halves precision
    if precision == PRECISION_HALVES:
        return round(temperature * 2) / 2
    #convert to tenths precision
    elif precision == PRECISION_TENTHS:
        return round(temperature, 1)
    
    # convert to Whole number
    return round(temperature)


#shows temperature in all different units of measurement
def differents_units_of_measurement(
    hass: HomeAssistant, temperature: float | None, precision: str
    )-> dict[str, float | None]:
    """Get temperature in all different units of measurement."""
    return {
        TEMP_CELSIUS: display_temp(hass, temperature, TEMP_CELSIUS, precision),
        TEMP_FAHRENHEIT: display_temp(hass, temperature, TEMP_FAHRENHEIT, precision),
        TEMP_KELVIN: display_temp(hass, temperature, TEMP_KELVIN, precision),
    }