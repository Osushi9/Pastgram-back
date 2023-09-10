from flask import Blueprint, Response, jsonify, make_response, request
from api.lib.storage import upload_image, download_image

# ルーティング設定
storage_router = Blueprint("storage_router", __name__)

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
    image_data, content_type = download_image(image_path)
    response = Response(image_data, content_type=content_type)
    return response
