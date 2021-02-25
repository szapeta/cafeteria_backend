
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
import mysql.connector
import pymysql
import info
import productos

app = Flask(__name__)
app.secret_key = 'mysmd@'


@app.route('/', methods=['GET'])
def index():
    return jsonify(info.getInfo())


@app.route('/productos', methods=['GET'])
def getProductos():
    return jsonify(productos.getallproducts())


if __name__ == '__main__':
    app.run(debug=True, port=8081)