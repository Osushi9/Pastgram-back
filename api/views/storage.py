from flask import Blueprint, Response, request, make_response, jsonify
from config import AwsClient, BucketName
import json
import uuid

# ルーティング設定
storage_router = Blueprint("storage_router", __name__)

def upload_image(file):
    filename = str(uuid.uuid1())
    AwsClient.upload_fileobj(file.stream, BucketName, filename)
    return filename

def download_image(filename):
    response = AwsClient.get_object(Bucket=BucketName, Key=filename)
    return response['Body'].read()

@storage_router.route("/upload", methods=["POST"])
def Upload():
    if 'image' not in request.files:
        return make_response(jsonify({"code": 401, "message": "image is not included."}))
    
    file = request.files['image']

    filename = upload_image(file)

    return make_response(jsonify({"image_path": filename}))

@storage_router.route("/download", methods=["GET"])
def Download():
    filename = request.args.get('filename')
    mime = request.args.get('mime')
    image_data = download_image(filename)
    response = Response(image_data, content_type=mime)
    return response
