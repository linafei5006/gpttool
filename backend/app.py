from flask import Flask, render_template, request, jsonify
from templates.chatgpt import get_response_from_gpt
from templates.draw import generate_image

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/draw')
def draw():
    return render_template('draw.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    text = request.form['text']
    response = get_response_from_gpt(text)
    return jsonify({'response': response})

@app.route('/generate_image', methods=['POST'])
def generate():
    text = request.form['text']
    image = generate_image(text)
    return jsonify({'image': image})

if __name__ == '__main__':
    app.run(debug=True)
