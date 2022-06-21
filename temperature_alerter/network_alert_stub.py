threshold_limit = 100


def network_alert_stub(celcius):
    print(f"ALERT: Temperature is {celcius} celcius")
    return 200 if celcius <= threshold_limit else 500
