import time
from datetime import datetime, timedelta
from flask import Flask, render_template, url_for, request
import json
import matplotlib
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np

app = Flask(__name__)
matplotlib.use('Agg')

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

# @app.route('/test')
# def test():
#     return render_template("index.html")


def one_investment_strategy(data, amount, strategy):
    list_of_stocks = []
    current_worth = 0
    investment_amount = int(amount)
    arr = []

    # Go through the list of stocks one by one
    for stock_element in data[strategy]:
        stock_info = []
        stock_portfolio = []
        percentage_of_stock = (int(stock_element['percentage']) / 100)
        amount_invested = percentage_of_stock * investment_amount
        print("Money invested in", stock_element['name'], "is", amount_invested)
        stock = yf.Ticker(stock_element['symbol'])

        if strategy == 'Ethical Investing':
            curr_price = stock.info['currentPrice']

        elif strategy == 'Growth Investing':
            curr_price = stock.info['currentPrice']

        elif strategy == 'Index Investing':
            curr_price = stock.info['navPrice']

        elif strategy == 'Quality Investing':
            curr_price = stock.info['currentPrice']

        elif strategy == 'Value Investing':
            curr_price = stock.info['currentPrice']

        print("The current value of the stock", stock_element['name'], "is ", curr_price)

        # Storing the name of the stock
        stock_info.append(stock_element['name'])
        # Storing the amount invested in this specific stock
        stock_info.append(amount_invested)
        # Storing the current price of the stock
        stock_info.append(curr_price)

        arr.append(stock_info)

        history = stock.history(period="5d")
        no_of_shares = amount_invested / curr_price
        i = 0
        for price in history['Close']:
            print(price, i)
            stock_portfolio.append(price * no_of_shares)
        list_of_stocks.append(stock_portfolio)

        print(len(list_of_stocks[i]))
        i += 1
        current_worth += (curr_price * no_of_shares)

    # changes
    total_portfolio = []
    # print(list_of_stocks)
    for index in range(len(list_of_stocks[0])):
        s = 0
        s = s + list_of_stocks[0][index] + list_of_stocks[1][index] + \
            list_of_stocks[2][index] + list_of_stocks[3][index]
        total_portfolio.append(s)
    print(total_portfolio)

    # new

    dates = get_dates()
    print(dates)
    print(total_portfolio)
    print(current_worth)

    plot_chart(dates, total_portfolio, data, strategy)

    return arr


def get_dates():
    now = datetime.now()
    curr_day = now.strftime('%m-%d-%Y')

    d = str(curr_day)
    d1 = datetime.strptime(d, '%m-%d-%Y')
    dates = [(d1 - timedelta(days=i)).strftime('%m-%d-%Y') for i in range(5, 0, -1)]
    return dates


def plot_chart(dates, total_portfolio, data, strategy):
    print(len(dates), len(total_portfolio))
    plt.clf()
    plt.plot(dates, total_portfolio)
    plt.xlabel("Last 5 days")
    plt.ylabel("Amount in USD")
    plt.title("Overall Portfolio Trend")
    plt.savefig('static/images/investment-strategy.jpeg')
    pie_one_investment = np.array([])
    pie_labels = []
    for stock_item in data[strategy]:
        pie_one_investment = np.append(pie_one_investment, int(stock_item['percentage']))
        pie_labels.append(stock_item['name'])
    plt.clf()
    plt.title("Distribution of money towards each stock")

    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    explode = (0.05, 0.05, 0.05, 0.05)

    plt.pie(pie_one_investment, labels=pie_labels, startangle=90, pctdistance=0.85, explode=explode)
    plt.savefig('static/images/pie_chart-investment-strategy.jpeg')


def two_investment_strategy(data, amount, strategy1, strategy2):
    list_of_stocks = []
    current_worth = 0
    investment_amount = int(int(amount)/2)
    arr = []

    # Go through the list of stocks one by one
    for stock_element in data[strategy1]:
        stock_info = []
        stock_portfolio = []
        percentage_of_stock = (int(stock_element['percentage']) / 100)
        amount_invested = percentage_of_stock * investment_amount
        print("Money invested in", stock_element['name'], "is", amount_invested)
        stock = yf.Ticker(stock_element['symbol'])

        if strategy1 == 'Ethical Investing':
            curr_price = stock.info['currentPrice']

        elif strategy1 == 'Growth Investing':
            curr_price = stock.info['currentPrice']

        elif strategy1 == 'Index Investing':
            curr_price = stock.info['navPrice']

        elif strategy1 == 'Quality Investing':
            curr_price = stock.info['currentPrice']

        elif strategy1 == 'Value Investing':
            curr_price = stock.info['currentPrice']

        print("The current value of the stock", stock_element['name'], "is ", curr_price)

        # Storing the name of the stock
        stock_info.append(stock_element['name'])
        # Storing the amount invested in this specific stock
        stock_info.append(amount_invested)
        # Storing the current price of the stock
        stock_info.append(curr_price)

        arr.append(stock_info)

        stock = yf.Ticker(stock_element['symbol'])

        history = stock.history(period="5d")
        no_of_shares = amount_invested / curr_price
        i = 0
        for price in history['Close']:
            print(price, i)
            stock_portfolio.append(price * no_of_shares)
        print("Added")
        list_of_stocks.append(stock_portfolio)

        current_worth += (curr_price * no_of_shares)
    for stock_element in data[strategy2]:
        stock_info = []
        stock_portfolio = []
        percentage_of_stock = (int(stock_element['percentage']) / 100)
        amount_invested = percentage_of_stock * investment_amount
        print("Money invested in", stock_element['name'], "is", amount_invested)
        stock = yf.Ticker(stock_element['symbol'])

        if strategy2 == 'Ethical Investing':
            curr_price = stock.info['currentPrice']

        elif strategy2 == 'Growth Investing':
            curr_price = stock.info['currentPrice']

        elif strategy2 == 'Index Investing':
            curr_price = stock.info['navPrice']

        elif strategy2 == 'Quality Investing':
            curr_price = stock.info['currentPrice']

        elif strategy2 == 'Value Investing':
            curr_price = stock.info['currentPrice']

        print("The current value of the stock", stock_element['name'], "is ", curr_price)

        # Storing the name of the stock
        stock_info.append(stock_element['name'])
        # Storing the amount invested in this specific stock
        stock_info.append(amount_invested)
        # Storing the current price of the stock
        stock_info.append(curr_price)

        arr.append(stock_info)
        stock = yf.Ticker(stock_element['symbol'])


        history = stock.history(period="5d")
        no_of_shares = amount_invested / curr_price
        i = 0
        for price in history['Close']:
            print(price, i)
            stock_portfolio.append(price * no_of_shares)
        list_of_stocks.append(stock_portfolio)

        current_worth += (curr_price * no_of_shares)

    print(list_of_stocks)


    total_portfolio = []
    for index in range(len(list_of_stocks[0])):
        s = 0
        s = s + list_of_stocks[0][index] + list_of_stocks[1][index] + \
            list_of_stocks[2][index] + list_of_stocks[3][index] + list_of_stocks[4][index] + list_of_stocks[5][index] + \
            list_of_stocks[6][index] + list_of_stocks[7][index]
        total_portfolio.append(s)
    print(total_portfolio)

    dates = get_dates()
    print(dates)
    print(total_portfolio)
    print(current_worth)
    pltGraph_twoInvestment(dates, data, strategy1, strategy2, total_portfolio)
    return arr


def pltGraph_twoInvestment(dates, data, strategy1, strategy2, total_portfolio):
    plt.clf()
    plt.plot(dates, total_portfolio)
    plt.xlabel("Last 5 days")
    plt.ylabel("Amount in USD")
    plt.title("Overall Portfolio Trend")
    plt.savefig('static/images/two_investment-strategy.jpeg')
    pie_two_investment = np.array([])
    pie_labels = []
    for stock_item in data[strategy1]:
        pie_two_investment = np.append(pie_two_investment, int(stock_item['percentage']) / 2)
        pie_labels.append(stock_item['name'])
    for stock_item in data[strategy2]:
        pie_two_investment = np.append(pie_two_investment, int(stock_item['percentage']) / 2)
        pie_labels.append(stock_item['name'])
    plt.clf()
    plt.title("Distribution of money towards each stock")
    plt.pie(pie_two_investment, labels=pie_labels)
    plt.savefig('static/images/pie_chart-two-investment-strategy.jpeg')


@app.route('/result', methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    name = output["name"]
    strategy = output["strategy"]
    with open('investing_strategies.json') as f:
        data = json.load(f)
    print(data)
    l = strategy.split()
    if len(strategy.split()) == 2:
        info = one_investment_strategy(data, name, strategy)
        stock1 = info[0][0]
        stock2 = info[1][0]
        stock3 = info[2][0]
        stock4 = info[3][0]
        stock1_price = info[0][2]
        stock2_price = info[1][2]
        stock3_price = info[2][2]
        stock4_price = info[3][2]
        stock1_money = info[0][1]
        stock2_money = info[1][1]
        stock3_money = info[2][1]
        stock4_money = info[3][1]
        return render_template('one_strategy.html', name=name, strategy=strategy, stock1=stock1, stock2=stock2,
                               stock3=stock3, stock4=stock4, stock1_price=stock1_price, stock2_price=stock2_price,
                               stock3_price=stock3_price, stock4_price=stock4_price, stock1_money=stock1_money,
                               stock2_money=stock2_money, stock3_money=stock3_money, stock4_money=stock4_money,
                               url='static/images/investment-strategy.jpeg',
                               url_pie='static/images/pie_chart-investment-strategy.jpeg')
    else:
        amount = int(name)
        strategy1_list = l[0:2]
        strategy2_list = l[3:]
        strategy1 = ' '.join(strategy1_list)
        strategy2 = ' '.join(strategy2_list)
        info = two_investment_strategy(data, amount, strategy1, strategy2)
        stock1 = info[0][0]
        stock2 = info[1][0]
        stock3 = info[2][0]
        stock4 = info[3][0]
        stock1_price = info[0][2]
        stock2_price = info[1][2]
        stock3_price = info[2][2]
        stock4_price = info[3][2]
        stock1_money = info[0][1]
        stock2_money = info[1][1]
        stock3_money = info[2][1]
        stock4_money = info[3][1]
        stock5 = info[4][0]
        stock6 = info[5][0]
        stock7 = info[6][0]
        stock8 = info[7][0]
        stock5_price = info[4][2]
        stock6_price = info[5][2]
        stock7_price = info[6][2]
        stock8_price = info[7][2]
        stock5_money = info[4][1]
        stock6_money = info[5][1]
        stock7_money = info[6][1]
        stock8_money = info[7][1]
        return render_template('two_strategies.html', name=name, strategy=strategy1, strategy2=strategy, stock1=stock1,
                               stock2=stock2, stock3=stock3, stock4=stock4, stock5=stock5, stock6=stock6, stock7=stock7,
                               stock8=stock8, stock1_price=stock1_price, stock2_price=stock2_price,
                               stock3_price=stock3_price, stock4_price=stock4_price, stock5_price=stock5_price,
                               stock6_price=stock6_price, stock7_price=stock7_price, stock8_price=stock8_price,
                               stock1_money=stock1_money, stock2_money=stock2_money, stock3_money=stock3_money,
                               stock4_money=stock4_money, stock5_money=stock5_money, stock6_money=stock6_money,
                               stock7_money=stock7_money, stock8_money=stock8_money,
                               url='static/images/two_investment-strategy.jpeg',
                               url_pie='static/images/pie_chart-two-investment-strategy.jpeg')


if __name__ == "__main__":
    app.run(debug=True)
