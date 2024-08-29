from flask import Flask, render_template, request
from predictions import predict
import os
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method == 'POST':
        file = request.files['file']
        # Generate a unique filename using uuid
        unique_filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[-1]
        filename = "static/" + unique_filename
        
        
        try:
            # Save the file
            file.save(filename)
            model = request.form['model']
            prediction = predict(filename, model)
            return render_template('index.html', prediction=prediction, image_file=filename)
        except Exception as e:
            return render_template('index.html', error="Error processing image. Please upload a valid image file.", image_file=None)

if __name__ == '__main__':
    app.run(debug=True)
