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

        print(sql)
        cursor.execute(sql)
        ds = cursor.fetchall()
        return ds
    except Exception as e:
        print(e)


def selectCustom(query):
    try:
        conexion = mysql.connector.connect(**dbConnect)
        cursor = conexion.cursor()
        cursor.execute(query)
        ds = cursor.fetchall()
        return ds
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conexion.close()

def insert(tabla, campos, valores):
    try:
        conexion = mysql.connector.connect(**dbConnect)
        cursor = conexion.cursor()
        sql = 'insert into '+tabla+' ('+campos+') values ('+valores+');'
        cursor.execute(sql)
        conexion.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        cursor.close()
        conexion.close()

def update():
    
    return ""

def delete():
    
    return ""