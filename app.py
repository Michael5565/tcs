from flask import Flask, render_template, request, redirect, url_for
from blockchain import Blockchain, Block  # Assuming your blockchain code is in blockchain.py

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html', title='Hash Group 12', chain=blockchain.chain)

@app.route('/add_block', methods=['GET', 'POST'])
def add_block():
    if request.method == 'POST':
        data = request.form['data']
        blockchain.add_block(data)
        return redirect(url_for('index'))
    return render_template('add_block.html', title='Add New Block')

if __name__ == '__main__':
    app.run(debug=True)