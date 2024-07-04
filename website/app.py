from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('trial.html')

@app.route('/content/<filename>')
def get_content(filename):
    file_path = os.path.join('signs', filename)
    content = None
    with open(file_path, 'r') as file:
        content = file.read()
    return jsonify(content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4000)
