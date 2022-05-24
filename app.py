# from tensorflow import keras
# from tensorflow.keras import layers
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

from model.NeuralNetwork import NeuralNetwork

app = Flask(__name__)
app.config["ENV"] = "development"
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

loaded_model = NeuralNetwork()


# image_to_test = r'static/img/003_4v9BJPhzwVo.jpg'
# loaded_model.image_to_prediction([image_to_test])


@app.route('/')
def home():
    """Renders the home template"""
    print(app.config)
    return render_template('home.html')


@app.route('/analysis', methods=["GET", "POST"])
def analysis():
    """Takes a given image, passes it through the neural network and returns the predicted genus, user uploaded image,
    and generated prediction graph to the analysis.html template. Verifies the file uploaded is valid and secure."""
    if request.method == "POST":
        if request.files:

            image = request.files["image"]

            if image.filename == "":
                flash("Image must have a filename")
                # return redirect(request.url)
                return redirect('/')

            if not allowed_file(image.filename):
                flash("Invalid file type, upload a .jpg or .png file")
                return redirect('/')
            else:
                filename = secure_filename(image.filename)
            image_to_process = os.path.join(app.config["IMAGE_UPLOADS"], filename)
            print(image_to_process)
            image.save(image_to_process)

            print(f"Images Saved: {image_to_process}")
            top_prediction, graph_location = loaded_model.image_to_prediction([image_to_process])
            print(top_prediction)
            print(f"Request.url = {request.url}")
            return render_template('analysis.html', top_prediction=top_prediction,
                                   image_to_process=image_to_process, graph_location=graph_location)
    return redirect("/")


def allowed_file(filename):
    """Verifies that a given file name has an extension and has an allowed file extension per the ALLOWED_EXTENSIONS"""
    if not "." in filename:
        return False
    file_extension = filename.rsplit('.', 1)[1].lower()
    if file_extension in app.config["ALLOWED_EXTENSIONS"]:
        return True
    else:
        return False


# TODO: change debug=False before deployment
if __name__ == '__main__':
    app.run()
