from flask import Flask, render_template, request
from convert import to_usd, from_usd, CurrencyNotSupportedError, InvalidAmountError

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['from_currency'].upper()
    amount = float(request.form['amount'])
    to_currency = request.form['to_currency'].upper()

    try:
        amount_usd = to_usd(from_currency, amount)
        converted_amount = from_usd(to_currency, amount_usd)
        result = f"{amount} {from_currency} is {converted_amount} {to_currency}"
    except (CurrencyNotSupportedError, InvalidAmountError) as e:
        result = str(e)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)