

from . import app

@app.template_filter('roundDecimals')
def roundNumbers(nr):
    return round(nr, 2);