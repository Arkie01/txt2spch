from flask import Flask, render_template, request
import pyttsx3
import PyPDF2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)

        pdf_reader = PyPDF2.PdfReader(uploaded_file.filename)
        pages = len(pdf_reader.pages)

        player = pyttsx3.init()

        text_content = []
        for num in range(0, pages):
            page = pdf_reader.pages[num]
            text_content.append(page.extract_text())
        
        return render_template('result.html', text_content=text_content)

if __name__ == '__main__':
    app.run(debug=True)
