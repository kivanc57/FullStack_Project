from flask import Flask, render_template, request, redirect, url_for

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

    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        json_data = get_form_data()

        if json_data.get('input_text'):
            return render_template('file_analyze.html', input_text=json_data['input_text'])
        elif json_data.get('directory_name') and json_data.get('word_phrase_input'):
            return redirect(url_for('linguistic_data',
                                    directory_name=json_data['directory_name'],
                                    word_phrase_input=json_data['word_phrase_input']))

    return render_template('index.html')

@app.route('/file_analyze', methods=['POST'])
def file_analyze():
    import os
    directory_name = request.form.get('directory_name')
    word_phrase_input = request.form.get('word_phrase_input')
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
        
    return render_template('file_analyze.html', my_sents=my_sents, my_files=my_files)


@app.route('/linguistic_data', methods=['POST'])
def linguistic_data():
    if 'input_file' in request.files:
        uploaded_file = request.files['input_file']

        if uploaded_file.filename != '':
            file_content = uploaded_file.read().decode('utf-8')

            
            

            return render_template('linguistic_data.html', file_content=file_content)

    json_data = get_form_data()
    input_text = json_data.get('input_text')
    
    # For demonstration purposes, I'm just printing the input_text
    print(f'File analysis logic for: {input_text}')
    return render_template('file_analyze.html', input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)