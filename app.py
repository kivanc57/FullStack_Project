from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function to handle common form data retrieval and return as JSON
def get_form_data():
    input_text = request.form.get('input_text', None)
    directory_name = request.form.get('directory_name', None)
    word_phrase_input = request.form.get('word_phrase_input', None)

    data = {
        'input_text': input_text,
        'directory_name': directory_name,
        'word_phrase_input': word_phrase_input
    }

    return jsonify(data)

# REMOVE PRINTS IN THE END

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        json_data = get_form_data()

        if json_data.get('input_text'):
            try:
                print(json_data['input_text'])
                return render_template('file_analyze.html', input_text=json_data['input_text'])
            except Exception as e:
                print(f'Error processing text file: {str(e)}')

        elif json_data.get('directory_name') and json_data.get('word_phrase_input'):
            try:
                print(json_data['directory_name'])
                print(json_data['word_phrase_input'])
                return render_template('linguistic_data.html',
                                       directory_name=json_data['directory_name'],
                                       word_phrase_input=json_data['word_phrase_input'])
            except Exception as e:
                print(f'Error processing search: {str(e)}')

    return render_template('index.html')


@app.route('/file_analyze', methods=['POST'])
def file_analyze():
    json_data = get_form_data()

    if json_data.get('input_text') is not None:
        try:
            print(json_data['input_text'])
            return render_template('file_analyze.html', input_text=json_data['input_text'])
        except Exception as e:
            print(f'Error processing text file: {str(e)}')

    return render_template('file_analyze.html', input_text=None)


@app.route('/linguistic_data', methods=['POST'])
def linguistic_data():
    json_data = get_form_data()

    if json_data.get('directory_name') is not None and json_data.get('word_phrase_input') is not None:
        try:
            print(json_data['directory_name'])
            print(json_data['word_phrase_input'])

            import os, re
            user_path = json_data.get('directory_name')
            directory = os.listdir(user_path)

            word_phrase = json_data['word_phrase_input']
            
            for fname in directory:
                file_path = os.path.join(user_path + fname)

                if os.path.isFile(file_path):
                    with open(user_path, mode='r', encoding='utf-8') as f:
                        if word_phrase in f.read():
                            expression = '[^.]* ' + word_phrase ' [^.]*\.'
                            founding = re.search(expression, f)
                            word = founding.string 

                        
            



            return render_template('linguistic_data.html',
                                   directory_name=json_data['directory_name'],
                                   word_phrase_input=json_data['word_phrase_input'])
        except Exception as e:
            print(f'Error processing search: {str(e)}')

    return render_template('linguistic_data.html', dir_word=None)

if __name__ == '__main__':
    app.run(debug=True)