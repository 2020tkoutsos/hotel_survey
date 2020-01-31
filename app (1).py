from flask import Flask
from flask import render_template, request
import hotel
from hotel import quizAI

app = Flask(__name__)
app.debug = True

@app.route('/quiz', methods=['POST'])
def quiz():
    out1 = [request.form['radioButtonsQuestion1'], request.form['radioButtonsQuestion2'], request.form['radioButtonsQuestion3'], request.form['radioButtonsQuestion4']]
    out = 'YOUR FINAL HOTEL IS: ' + quizAI(out1)
    return render_template('index.html', out=out)

@app.route('/', methods=['GET'])
def index():
    out = ''
    return render_template('index.html', out=out)

@app.route('/order', methods=['POST'])
def order_now():
    order1 = Order()
    item1_1 = Item()
    order1.id = request.form['order_id']
    item1_1.type = request.form['order_item']
    #day = request.form['day']
    order1.items = [item1_1]

    orders = [order1]
    #get orders in order of their importance
    ordered_orders = order_orders(orders)
    #assign the orders to each day of the work week
    work_week = assign_time(ordered_orders, 100)
    #print out new schedule
    out = output_table(work_week)

    return render_template('base.html', out=out)

    
if __name__ == '__main__':
    app.run()