from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()


dbConnect = {
    "host":os.getenv("host"),
    "user":os.getenv("user"),
    "password":os.getenv("password"),
    "database":os.getenv("database")
}

def select(campos, tabla, condicion):
    try:
        conexion = mysql.connector.connect(**dbConnect)
        cursor = conexion.cursor()

        if len(condicion) > 0:
            sql = 'select '+campos+' from '+tabla+' where '+condicion+';'
        else:
            sql = 'select '+campos+' from '+tabla+';'

        cursor.execute(sql)
        ds = cursor.fetchall()
        return ds
    except Exception as e:
        print(e)
        
    finally:
        cursor.close()
        conexion.close()