from flask import Flask, render_template, request, jsonify
import math
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    
    try:
        a = float(data['a'])
        b = float(data['b'])
        c = float(data['c'])
        method = data['method']
    except:
        return jsonify({'error': 'Введите корректные числа!'})
    if a == 0:
        return jsonify({'error': 'Коэффициент a не может быть равен 0!'})
    D = b**2 - 4*a*c
    steps = ''
    result = ''
    x1 = None
    x2 = None
    if method == 'discriminant':
        steps += f'=== Метод дискриминанта ===\n\n'
        steps += f'Уравнение: {a}x² + {b}x + {c} = 0\n\n'
        steps += f'Шаг 1. Вычислить дискриминант:\n'
        steps += f'D = b² - 4ac\n'
        steps += f'D = ({b})² - 4·({a})·({c})\n'
        steps += f'D = {b**2} - {4*a*c} = {D}\n\n'
        steps += f'Шаг 2. Анализ D:\n'
        if D > 0:
            sqrtD = math.sqrt(D)
            x1 = (-b + sqrtD) / (2*a)
            x2 = (-b - sqrtD) / (2*a)
            steps += f'D > 0 → два корня\n\n'
            steps += f'Шаг 3. Вычислить корни:\n'
            steps += f'√D = {sqrtD:.4f}\n'
            steps += f'x1 = (-b + √D) / 2a = {x1:.4f}\n'
            steps += f'x2 = (-b - √D) / 2a = {x2:.4f}\n\n'
            steps += f'Ответ: x1 = {x1:.4f},  x2 = {x2:.4f}'
            result = f'x1 = {x1:.4f},  x2 = {x2:.4f}'
        elif D == 0:
            x1 = x2 = -b / (2*a)
            steps += f'D = 0 → один корень\n\n'
            steps += f'x = -b / 2a = {x1:.4f}\n\n'
            steps += f'Ответ: x1 = x2 = {x1:.4f}'
            result = f'x1 = x2 = {x1:.4f}'
        else:
            steps += f'D < 0 → вещественных корней нет\n\n'
            steps += f'Ответ: корней нет'
            result = 'Корней нет'
    else:
        steps += f'=== Теорема Виета ===\n\n'
        steps += f'Уравнение: {a}x² + {b}x + {c} = 0\n\n'
        if D < 0:
            steps += f'D = {D} < 0 → корней нет\n\n'
            steps += f'Ответ: корней нет'
            result = 'Корней нет'
        else:
            S = -b / a
            P = c / a
            sqrtD = math.sqrt(D)
            x1 = (S + sqrtD) / 2
            x2 = (S - sqrtD) / 2
            steps += f'Шаг 1. По теореме Виета:\n'
            steps += f'x1 + x2 = -b/a = {S}\n'
            steps += f'x1 * x2 =  c/a = {P}\n\n'
            steps += f'Шаг 2. D = S² - 4P = {D}\n\n'
            steps += f'x1 = (S + √D) / 2 = {x1:.4f}\n'
            steps += f'x2 = (S - √D) / 2 = {x2:.4f}\n\n'
            steps += f'Ответ: x1 = {x1:.4f},  x2 = {x2:.4f}'
            result = f'x1 = {x1:.4f},  x2 = {x2:.4f}'

    return jsonify({
        'result': result,
        'steps': steps,
        'x1': x1,
        'x2': x2,
        'a': a,
        'b': b,
        'c': c,
        'D': D,
        'method': method
    })
if __name__ == '__main__':
    app.run(debug=True)
