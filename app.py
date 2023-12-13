# Import libraries
from flask import Flask, render_template, request

# Start Flask
app = Flask(__name__)

# Global Variables for Text File Search API
directoryName, wtInput = None, None

# Global Variable for Linguistic Data of Text API
inputText = None

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/file_analyze', methods=['GET', 'POST'])
def file_analyze():
    return render_template('file_analyze.html')

@app.route('/linguistic_data', methods=['GET', 'POST'])
def linguistic_data():
    return render_template('linguistic_data.html')

if __name__ == '__main__':
    app.run(debug=True)