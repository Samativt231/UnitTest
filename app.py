from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        figure = request.form.get('figure')
        param1 = float(request.form.get('param1'))
        param2 = request.form.get('param2')
        precision = int(request.form.get('precision'))

        if figure == 'cube':
            result = param1 ** 3
        elif figure == 'sphere':
            result = (4/3) * math.pi * (param1 ** 3)
        elif figure == 'cylinder':
            if param2:
                param2 = float(param2)
                result = math.pi * (param1 ** 2) * param2
            else:
                result = "Введите второй параметр для цилиндра."

        if isinstance(result, float):
            result = f"{result:.{precision}f}"

    return render_template('index.html', result=result)