# Build Trading Model and estimator stock prices using Flask, Pandas and SQLite
# Developer: Neobytes
# Import Libraries
from flask import Flask, jsonify, request
from flask.globals import request
from flask.helpers import url_for
import random
import pandas as pd
import sqlite3
app = Flask(__name__)

# Build Trading Model and estimator stock prices using Flask and Pandas

# Create DataFrame to Model Stock Prices

trading = {
    'id_stock': ['S01', 'S02', 'S03', 'S04', 'S05', 'S06','S07','S08'],
    'id_broker': ['B01', 'B02', 'B03', 'B04', 'B05', 'B06','B07','B08'],
    'id_strategy': ['T01', 'T02', 'T03', 'T04', 'T05', 'T06','T07','T08'],
    'id_account': ['A01', 'A02', 'A03', 'A04', 'A05', 'A06','A07','A08'],
    'initial_investemnt': [10000, 20000, 30000, 40000, 50000, 60000,70000,80000],
    'current_investment': [10000, 20000, 30000, 40000, 50000, 60000,70000,80000],
    'buy_price': [100, 200, 300, 400, 500, 600,700,800],
    'sell_price': [120, 220, 320, 420, 520, 620,720,820],
    'buy_date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05', '2021-01-06','2021-01-07','2021-01-08'],
    'sell_date': ['2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05', '2021-01-06', '2021-01-07','2021-01-08','2021-01-09'],
    'profit_loss': [20, 40, 60, 80, 100, 120,140,160],
    'profit_loss_percent': [0.2, 0.4, 0.6, 0.8, 1.0, 1.2,1.4,1.6],
    'profit_loss_percent_cum': [0.2, 0.6, 1.2, 1.8, 2.4, 3.0,3.6,4.2],
    'profit_loss_percent_cum_avg': [0.2, 0.6, 1.2, 1.8, 2.4, 3.0,3.6,4.2],
    'profit_loss_percent_cum_max': [0.2, 0.6, 1.2, 1.8, 2.4, 3.0,3.6,4.2],
    'asset':['crypto','gold','silver','stock','bond','commodity','USDT','ethereum'],
    'quantity': [100, 200, 300, 400, 500, 600,700,800],
    'trading_rating': [18.5, 17.5, 16.5, 15.5, 14.5, 13.5,12.5,11.5]
    
}
data_trading = pd.DataFrame(trading)
# Print DataFrame
print(data_trading)

# Calculate Profit and Loss

def calculate_profit_loss(data_trading):
    data_trading['profit_loss'] = data_trading['sell_price'] - data_trading['buy_price']
    data_trading['profit_loss_percent'] = (data_trading['profit_loss'] / data_trading['buy_price']) * 100
    data_trading['profit_loss_percent_cum'] = data_trading['profit_loss_percent_cum'].fillna(0) + data_trading['profit_loss_percent']
    data_trading['profit_loss_percent_cum_avg'] = data_trading['profit_loss_percent_cum'].rolling(window=20).mean()
    data_trading['profit_loss_percent_cum_max'] = data_trading['profit_loss_percent_cum'].rolling(window=20).max()
    return data_trading

# Print DataFrame with Profit and Loss
data_trading = calculate_profit_loss(data_trading)
print(data_trading)

# Calculate trading rating
def calculate_trading_rating(data_trading):
    data_trading['trading_rating'] = data_trading['profit_loss_percent_cum_avg']
    return data_trading

# Print DataFrame with trading rating
data_trading = calculate_trading_rating(data_trading)
print(data_trading)
# Calculate investment inital and current
def calculate_investment(data_trading):
    data_trading['initial_investment'] = data_trading['initial_investemnt']
    data_trading['current_investment'] = data_trading['current_investment'] + data_trading['profit_loss']
    return data_trading

# Print DataFrame with investment inital and current
data_trading = calculate_investment(data_trading)
print(data_trading)
# Save DataFrame to CSV file
data_trading.to_csv('trading.csv', index=False)

# Create API endpoints
# Endpoint to get all trading data
@app.route('/api/trading', methods=['GET'])
def get_trading():
    return jsonify(data_trading.to_dict(orient='records'))

# Endpoint to get trading data by id_stock
@app.route('/api/trading/<id_stock>', methods=['GET'])
def get_trading_by_id_stock(id_stock):
    trading_by_id_stock = data_trading[data_trading['id_stock'] == id_stock]
    return jsonify(trading_by_id_stock.to_dict(orient='records'))

# Endpoint to get trading data by id_broker
@app.route('/api/trading/broker/<id_broker>', methods=['GET'])
def get_trading_by_id_broker(id_broker):
    trading_by_id_broker = data_trading[data_trading['id_broker'] == id_broker]
    return jsonify(trading_by_id_broker.to_dict(orient='records'))

# Endpoint to get trading data by id_strategy
@app.route('/api/trading/strategy/<id_strategy>', methods=['GET'])
def get_trading_by_id_strategy(id_strategy):
    trading_by_id_strategy = data_trading[data_trading['id_strategy'] == id_strategy]
    return jsonify(trading_by_id_strategy.to_dict(orient='records'))
# Endpoint to get trading data by id_account
@app.route('/api/trading/account/<id_account>', methods=['GET'])
def get_trading_by_id_account(id_account):
    trading_by_id_account = data_trading[data_trading['id_account'] == id_account]
    return jsonify(trading_by_id_account.to_dict(orient='records'))

# Endpoint to get trading data by asset
@app.route('/api/trading/asset/<asset>', methods=['GET'])
def get_trading_by_asset(asset):
    trading_by_asset = data_trading[data_trading['asset'] == asset]
    return jsonify(trading_by_asset.to_dict(orient='records'))

# Create database
conn = sqlite3.connect('trading.db')

# Create table
data_trading.to_sql('trading', conn, if_exists='replace', index=False)

# Endpoint to save trading data
@app.route('/api/trading', methods=['POST'])
def save_trading():
    data = request.get_json()
    data_trading = pd.DataFrame(data)
    data_trading.to_sql('trading', conn, if_exists='append', index=False)
    return jsonify({'message': 'Data saved successfully!'})

# Endpoint to get all trading data from database
@app.route('/api/trading/db', methods=['GET'])
def get_trading_db():
    cursor = conn.execute("SELECT * FROM trading")
    data_trading_db = pd.DataFrame(cursor.fetchall())
    data_trading_db.columns = cursor.column_names
    return jsonify(data_trading_db.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)
    

        
    

