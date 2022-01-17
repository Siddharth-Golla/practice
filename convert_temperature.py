def convert_temperatures(temperature_unit: float, source_scale: str, target_scale: str) -> float:
    """Returns the converted temperature_unit from source_scale to target_scale

        conversion factor:
        313.15 Kelvin = 40 Celsius = 104 Fahrenheit = 563.67 Rankine = 28.5 Romer = 13.2 Newton = 90 Delisle = 32 Reaumur

    Args:
        temperature_unit (float): Unit of temperature to be converted
        source_scale (str): Scale of temperature_unit (e.g. Celsuis, Kelvin, etc)
        target_scale (str): Scale to which the temperature_unit is to be converted

    Returns:
        float: Converted temperature in target scale
    """

# Convert temperature from source scale to celsius scale

    if source_scale.lower() == "celsius":
        temperature_unit_in_celsius = temperature_unit
    elif source_scale.lower() == "fahrenheit":
        temperature_unit_in_celsius = (temperature_unit - 32)*(5/9)
    elif source_scale.lower() == "kelvin":
        temperature_unit_in_celsius = (temperature_unit - 273.5)
    elif source_scale.lower() == "rankie":
        temperature_unit_in_celsius = (temperature_unit - 491.67)*(5/9)
    elif source_scale.lower() == "delisle":
        temperature_unit_in_celsius = (100 - temperature_unit)*(2/3)
    elif source_scale.lower() == "newton":
        temperature_unit_in_celsius = (temperature_unit)*(100/3)
    elif source_scale.lower() == "reaumer":
        temperature_unit_in_celsius = (temperature_unit)*(5/4)
    else:
        print("Invalid source input")

# Convert temperature from celsius scale to target scale and return

    if target_scale.lower() == "celsius":
        return temperature_unit_in_celsius
    elif target_scale.lower() == "fahrenheit":
        return (temperature_unit_in_celsius * (9/5)) + 32
    elif target_scale.lower() == "kelvin":
        return temperature_unit_in_celsius + 273.15
    elif target_scale.lower() == "rankie":
        return (temperature_unit_in_celsius + 273.15) * (9/5)
    elif target_scale.lower() == "delise":
        return (100 - temperature_unit_in_celsius) * (3/2)
    elif target_scale.lower() == "newton":
        return temperature_unit_in_celsius * (33/100)
    elif target_scale.lower() == "reaumer":
        return temperature_unit_in_celsius * (4/5)
    else:
        print("Invalid target input")


# Driver code
if __name__ == "__main__":
    temperature = float(input("Enter temperature units: "))
    source = input(
        "Enter the source temperature scale (Options:celsius, fahrenheit, kelvin, rankie, delisle, newton, reaumer): ")
    target = input(
        "Enter the target temperature scale (Options:celsius, fahrenheit, kelvin, rankie, delisle, newton, reaumer): ")
    print(convert_temperatures(temperature, source, target))
