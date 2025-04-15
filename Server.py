from flask import Flask, request, render_template
from ImageGenerator import ImageGenerator
import os


app = Flask(__name__)
images_folder = os.path.join('static', 'images')
app.config["UPLOAD_FOLDER"] = images_folder
imageGen = ImageGenerator()


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        prompt = request.form["prompt"]
        image = imageGen.generate_image(prompt)
        image.save("static/images/image.png")
        saved_image = os.path.join(app.config["UPLOAD_FOLDER"], "image.png")
        return render_template('base.html', last_prompt=prompt, image=saved_image)
    else:
        return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=False)

