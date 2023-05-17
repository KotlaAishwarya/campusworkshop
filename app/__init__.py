"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7pbt269vf5qbaa44g-a.oregon-postgres.render.com",
        database="todo_di45",
        user="aishu",
        password="WO5oCWOK1JoPM6p3g2d2wCofIXIiZe7k")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
