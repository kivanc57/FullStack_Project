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

    return data  # Return a dictionary instead of using jsonify

# REMOVE PRINTS IN THE END

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        json_data = get_form_data()

        if json_data.get('input_text'):
            try:
                return render_template('file_analyze.html', input_text=json_data['input_text'])
            except Exception as e:
                print(f'Error processing text file: {str(e)}')

        elif json_data.get('directory_name') and json_data.get('word_phrase_input'):
            try:
                return render_template('linguistic_data.html',
                                       directory_name=json_data['directory_name'],
                                       word_phrase_input=json_data['word_phrase_input'])
            except Exception as e:
                print(f'Error processing search: {str(e)}')

    return render_template('index.html')


@app.route('/file_analyze', methods=['POST'])
def file_analyze():
    try:
        json_data = get_form_data()
        print(json_data['input_text'])

        return render_template('file_analyze.html', input_text=json_data['input_text'])
    except Exception as e:
        print(f'Error processing text file: {str(e)}')

    return render_template('file_analyze.html', input_text=None)


@app.route('/linguistic_data', methods=['POST'])
def linguistic_data():
    try:
        import os
        json_data = get_form_data()
        directory_name = json_data.get('directory_name')
        word_phrase_input = json_data.get('word_phrase_input')
        my_sents = []
        my_files = []

        for file in os.listdir(directory_name):
            if file.endswith('.txt'):
                text_path = os.path.join(directory_name, file)
                with open(text_path, mode='r') as f:
                    lines = f.readlines()
                    for line in lines:
                        if word_phrase_input in line:
                            sentences = line.split('.')
                            for sent in sentences:
                                if word_phrase_input in sent:
                                    if sent[0] == ' ':
                                        sent = sent[1:]
                                    my_sents.append(sent)
                                    my_files.append(file)

        if my_sents:
            my_sent = my_sents[0]
            my_file = my_files[0]
        else:
            my_sent = None
            my_file = None

        return render_template('linguistic_data.html', my_sent=my_sent, my_file=my_file)
    except Exception as e:
        print(f'Error processing search: {str(e)}')

    return render_template('linguistic_data.html', my_sent=None, my_file=None)

if __name__ == '__main__':
    app.run(debug=True)
