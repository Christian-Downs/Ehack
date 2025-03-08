from flask import Flask, render_template, request
from aiTester import caller
from fileNameParse import convert_text_to_json
from JsonToProject import jsonToProject



app = Flask(__name__)

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    # Example Usage:
    text = request.form['text']

    caller(text)
    file_path = 'input.txt'
    with open(file_path, 'r') as file:
        file_content = file.read()
        file.close()
    with open("Output.json", "w") as file:
        json_data = convert_text_to_json(file_content)
        file.write(json_data)
    jsonToProject(str(json_data))
    
    return "PROCESSED"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
