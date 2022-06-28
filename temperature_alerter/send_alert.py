import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from temperature_alerter.temperature_converter import convert_farenheit_to_celcius


alert_failure_count = 0


def alert_in_celcius(farenheit, network_alert):
    """
    (int, Callable) -> None

    accepts farenheit and function for networkalert
    alert_failure_count global variable is incremeted by 1 for every non-ok response from network_alert
    """
    celcius = convert_farenheit_to_celcius(farenheit)
    returnCode = network_alert(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1
