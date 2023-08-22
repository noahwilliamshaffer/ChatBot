'''This is the server file.'''
import sqlite3

# import http.client
import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for, request
from apscheduler.schedulers.background import BackgroundScheduler







if __name__ == "__main__":
    app.run(debug=True)