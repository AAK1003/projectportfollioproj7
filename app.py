from flask import Flask, render_template, url_for, abort

app = Flask(__name__)

PROJECTS = {
    'caluclator': {}
}