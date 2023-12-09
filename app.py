#Import libraries
from flask import Flask, render_template, request


#Start Flask
app = Flask(__name__)

#Global Variables for Text File Search API
directoryName, wtInput = None, None

#Global Variable for Linguistic Data of Text API
inputText = None
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('')

"""app.route('/fileTextSearch.html', methods=['GET', 'POST'])
def file_analyze():


@app.route('/linguisticDataText.html', methods=['GET', 'POST'])
def linguistic_data_text():"""

if __name__ == '__main__': 
    app.run(debug=True)