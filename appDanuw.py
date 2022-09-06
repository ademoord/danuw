#
# file: appDanuw.py
# author: andromeda
# desc: the main views and routes file
#
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    title = "Home"
    return render_template("index.html",
                            title=title
    )

@app.route('/product-detail-ps')
def product():
    title = "Pineapple Strudel"
    return render_template("/product/product-details-pineapple-strudel.html",
                            title=title
    )

@app.route('/cart')
def cart():
    return render_template("cart.html")
