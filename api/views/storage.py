import uuid
import mimetypes

from flask import Blueprint, Response, jsonify, make_response, request

from config import AwsClient, BucketName

# ルーティング設定
storage_router = Blueprint("storage_router", __name__)

mimetypes.init()


def upload_image(file):
    extension = mimetypes.guess_extension(file.filename)
    filename = str(uuid.uuid1()) + extension
    AwsClient.upload_fileobj(file.stream, BucketName, filename)
    return filename

def download_image(filename):
    response = AwsClient.get_object(Bucket=BucketName, Key=filename)
    return response["Body"].read()

@storage_router.route("/upload", methods=["POST"])
def Upload():
    if "image" not in request.files:
        return make_response(
            jsonify({"code": 401, "message": "image is not included."})
        )

    file = request.files["image"]

    image_path = upload_image(file)

    return make_response(jsonify({"code": 200, "image_path": image_path}))


@storage_router.route("/download", methods=["GET"])
def Download():
    image_path = request.args.get("image_path")
    image_data = download_image(image_path)
    content_type = mimetypes.guess_type(image_path)[0] or "image/jpeg"
    response = Response(image_data, content_type=content_type)
    return response
