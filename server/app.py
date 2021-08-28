import os, boto3
from flask import Flask, request, session
from werkzeug.utils import secure_filename
from flask_cors import CORS



ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

s3 = boto3.client('s3',
                    aws_access_key_id="XXXXXXXXXXXXXXXXXXXX",
                    aws_secret_access_key="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
                     )


BUCKET_NAME='XXXXXXXXXXXXXX'

app = Flask(__name__)

CORS(app, expose_headers='Authorization')


@app.route('/upload', methods=['POST'])
def upload():
    msg = "testing"
    if request.method == 'POST':
        img = request.files['image']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                os.remove(filename)
                msg = "upload done ! "
    return msg


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, port=8000)
