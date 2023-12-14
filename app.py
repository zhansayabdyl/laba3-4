from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_mortgage(principal, annual_rate, years):
# Проверяем, что значения положительные
    if principal <= 0 or annual_rate < 0 or years <= 0:
        raise ValueError("Все значения должны быть положительными")

    # Преобразуем годовую процентную ставку в месячную и количество лет в месяцы
    monthly_rate = annual_rate / 100 / 12
    num_payments = years * 12

    # Вычисляем ежемесячный платеж по формуле аннуитетного платежа
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate)**-num_payments)

    # Общая сумма, уплаченная по кредиту
    total_payment = monthly_payment * num_payments

    return monthly_payment, total_payment


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        principal = float(request.form.get('principal'))
        annual_rate = float(request.form.get('annual_rate'))
        years = int(request.form.get('years'))

        monthly_payment, total_payment = calculate_mortgage(principal, annual_rate, years)

        return render_template('index.html',
                               result=f'Ежемесячный платеж: {monthly_payment:.2f} руб. Общая сумма: {total_payment:.2f} руб.')
    except ValueError:
        return render_template('index.html', result='Пожалуйста, введите корректные значения.')


if __name__ == '__main__':
    app.run(debug=True)
