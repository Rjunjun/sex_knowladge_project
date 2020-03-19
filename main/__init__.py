from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
from .view import view
