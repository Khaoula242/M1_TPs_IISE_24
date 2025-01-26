def dollars_to_dirhams(dollars):
    if dollars<0:
        raise ValueError("la valeur doit être positive")
    else:
        return dollars*10.5

def meters_to_kilometers(meters):
    if meters<0:
        raise ValueError("la distance doit être positive")
    else:
        return meters/1000