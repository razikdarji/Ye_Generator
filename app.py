from flask import Flask, render_template, jsonify, request
from kanye import get_kanye_quote
from bot import generate_dalle_image
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/generate-image', methods=['GET'])
def generate_image():
    quote = get_kanye_quote()
    image = generate_dalle_image(quote)
    print(image)
    # For demonstration, let's assume 'image' is a URL to the generated image
    
    return jsonify({"quote": quote, "image": image})

if __name__ == '__main__':
    app.run(debug=True)
