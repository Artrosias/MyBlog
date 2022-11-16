import os
from flask import current_app
from myblog import app
from PIL import Image

UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']

def save_images(form_data):
    filename = form_data.filename
    picture_name = filename
    picture_path = os.path.join(current_app.root_path, UPLOAD_FOLDER, picture_name)

    image = image.open(form_data)
    image.save(picture_path)

    return picture_name