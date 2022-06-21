from temperature_alerter.send_alert import alert_in_celcius, alert_failure_count
from temperature_alerter.network_alert_stub import network_alert_stub

alert_in_celcius(400.5, network_alert_stub)
alert_in_celcius(303.6, network_alert_stub)
alert_in_celcius(201.8, network_alert_stub)
assert alert_failure_count == 2

print(f"{alert_failure_count} alerts failed.")
print("All is well")
