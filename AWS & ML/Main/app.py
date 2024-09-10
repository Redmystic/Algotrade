from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Exampro.html')

@app.route('/next')
def next_page():
    return render_template('next_page.html')

if __name__ == '__main__':
    app.run(debug=True)
