"""Tests Home Assistant temperature helpers."""
import pytest

from homeassistant.const import (
    PRECISION_HALVES,
    PRECISION_TENTHS,
    PRECISION_WHOLE,
    TEMP_CELSIUS,
    TEMP_FAHRENHEIT,
    TEMP_KELVIN,
)
from homeassistant.helpers.temperature import display_temp, differents_units_of_measurement, round_temperature

TEMP = 24.636626

def test_round_temperature(hass):
    """Test round_temperature."""
    assert round_temperature(TEMP, PRECISION_WHOLE) == 25
    assert round_temperature(TEMP, PRECISION_TENTHS) == 24.6
    assert round_temperature(TEMP, PRECISION_HALVES) == 24.5

def test_display_temp(hass):
    """Test display_temp."""
    assert display_temp(hass, TEMP, TEMP_CELSIUS, PRECISION_WHOLE) == 25
    assert display_temp(hass, TEMP, TEMP_FAHRENHEIT, PRECISION_WHOLE) == 76
    assert display_temp(hass, TEMP, TEMP_KELVIN, PRECISION_WHOLE) == 298

    assert display_temp(hass, TEMP, TEMP_CELSIUS, PRECISION_TENTHS) == 24.6
    assert display_temp(hass, TEMP, TEMP_FAHRENHEIT, PRECISION_TENTHS) == 76.3
    assert display_temp(hass, TEMP, TEMP_KELVIN, PRECISION_TENTHS) == 297.8

    assert display_temp(hass, TEMP, TEMP_CELSIUS, PRECISION_HALVES) == 24.5
    assert display_temp(hass, TEMP, TEMP_FAHRENHEIT, PRECISION_HALVES) == 76.5
    assert display_temp(hass, TEMP, TEMP_KELVIN, PRECISION_HALVES) == 298.0

def test_display_temp_no_temperature(hass):
    """Test display_temp with no temperature."""
    assert display_temp(hass, None, TEMP_CELSIUS, PRECISION_WHOLE) is None

def test_display_temp_invalid_temperature(hass):
    """Test display_temp with invalid temperature."""
    with pytest.raises(TypeError):
        display_temp(hass, "not a number", TEMP_CELSIUS, PRECISION_WHOLE)

def test_differents_units_of_measurement(hass):
    assert differents_units_of_measurement(hass, TEMP, PRECISION_WHOLE) == { 
        TEMP_CELSIUS: 25, 
        TEMP_FAHRENHEIT: 76, 
        TEMP_KELVIN:  298
        }
    assert differents_units_of_measurement(hass, TEMP, PRECISION_TENTHS) == { 
        TEMP_CELSIUS: 24.6, 
        TEMP_FAHRENHEIT: 76.3, 
        TEMP_KELVIN: 297.8
        }
    assert differents_units_of_measurement(hass, TEMP, PRECISION_HALVES) == { 
        TEMP_CELSIUS: 24.5,
        TEMP_FAHRENHEIT: 76.5, 
        TEMP_KELVIN: 298.0
        }