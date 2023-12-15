from flask import Flask, render_template, request, json

app = Flask(__name__)

#REMOVE PRINTS IN THE END

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        input_text = request.form.get('input_text')
        directory_name = request.form.get('directory_name')
        word_phrase_input = request.form.get('word_phrase_input')

        if input_text:
            try:
                print(input_text)
                return render_template('index.html', input_text=input_text)
            except Exception as e:
                print(f'Error processing text file: {str(e)}')

        elif directory_name and word_phrase_input:
            try:
                dir_word = {word_phrase_input: directory_name}
                print(directory_name)
                print(word_phrase_input)
                print(dir_word)
                return render_template('index.html', dir_word=dir_word)
            except Exception as e:
                print(f'Error processing search: {str(e)}')

    return render_template('index.html')


@app.route('/file_analyze', methods=['GET', 'POST'])
def file_analyze():
    #Get the variables as a JSON package
    data = json.loads(request.args.get('input_text'))
    return render_template('file_analyze.html', input_text=data)


@app.route('/linguistic_data', methods=['GET', 'POST'])
def linguistic_data():
    #Get the variables as a JSON package
    data = json.loads(request.args.get('dir_word'))
    return render_template('linguistic_data.html', dir_word=data)

if __name__ == '__main__':
    app.run(debug=True)