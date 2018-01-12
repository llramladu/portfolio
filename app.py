from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/logos")
def logos():
	return render_template('logos.html')

@app.route("/layouts")
def layouts():
	return render_template('layouts.html')

@app.route("/links")
def links():
	return render_template('links.html')

@app.route("/photos")
def photos():
	return render_template('photos.html')

@app.route("/projects")
def projects():
	return render_template('projects.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404