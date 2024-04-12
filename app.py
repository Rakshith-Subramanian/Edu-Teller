from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])

def summarize():
    text = request.form['text']
    print(text)
    summary = run_summarizer(text)
    return render_template('index.html', summary=summary)

def run_summarizer(text):
    command = f'jupyter nbconvert --to notebook --execute --stdout --ExecutePreprocessor.timeout=-1 --SIH.ipynb --input "{text}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout


if __name__ == '__main__':
    app.run(debug=True)
