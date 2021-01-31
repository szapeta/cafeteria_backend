
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
import mysql.connector
import pymysql
import info

app = Flask(__name__)
app.secret_key = 'mysmd@'


@app.route('/', methods=['GET'])
def index():
    return jsonify(info.getInfo())


if __name__ == '__main__':
    app.run(debug=True, port=8081)