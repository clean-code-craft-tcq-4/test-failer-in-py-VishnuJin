from temperature_alerter import send_alert
from temperature_alerter.temperature_converter import convert_farenheit_to_celcius
from temperature_alerter.send_alert import alert_in_celcius
from temperature_alerter.network_alert_stub import network_alert_stub
from exception_handlers import get_error_type

alert_in_celcius(400.5, network_alert_stub)  # resp 500 - failure
alert_in_celcius(303.6, network_alert_stub)  # resp 500 - failure
alert_in_celcius(201.8, network_alert_stub)  # resp 200 - success

assert send_alert.alert_failure_count == 2
assert f"{convert_farenheit_to_celcius(201.8):.2f}" == "94.33"
assert get_error_type(alert_in_celcius, "A", network_alert_stub) == TypeError
assert get_error_type(convert_farenheit_to_celcius, "A") == TypeError

print(f"{send_alert.alert_failure_count} alerts failed.")
print("All is well")
