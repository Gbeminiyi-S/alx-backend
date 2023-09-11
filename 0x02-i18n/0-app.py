#!/usr/bin/env python3
"""This moduke sets up a basic Flask app"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('0-index.html')
