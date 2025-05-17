from flask import Flask, request, render_template
from ImageGenerator import ImageGenerator
from Translator import TranslatorModule
import os


app = Flask(__name__)
images_folder = os.path.join('static', 'images')
app.config["UPLOAD_FOLDER"] = images_folder
imageGen = ImageGenerator()
translator = TranslatorModule()


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if imageGen.isBusy == False:
            imageGen.isBusy = True
            prompt = request.form["prompt"]
            translated_prompt = translator.translate_text(prompt)
            print(translated_prompt)
            image = imageGen.generate_image(translated_prompt)
            image.save("static/images/image.png")
            saved_image = os.path.join(app.config["UPLOAD_FOLDER"], "image.png")
            imageGen.isBusy = False
            return render_template('base.html', last_prompt=prompt, image=saved_image)
        else:
            return render_template('base.html', last_prompt=request.form["prompt"], isBusy=True)
    else:
        return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=False)

