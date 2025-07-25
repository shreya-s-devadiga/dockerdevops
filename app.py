from flask import Flask , jsonify
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Dockerized Python App with NumPy and Pandas!"

@app.route('/numpy')
def use_numpy():
    arr = np.array([1, 2, 3, 4, 5])
    mean_val = np.mean(arr)
    return jsonify({'array': arr.tolist(), 'mean': mean_val})

@app.route('/pandas')
def use_pandas():
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
    df = pd.DataFrame(data)
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
