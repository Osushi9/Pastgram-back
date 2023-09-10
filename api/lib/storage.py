import uuid
import mimetypes

from config import AwsClient, BucketName

mimetypes.init()

def upload_image(file):
    extension = mimetypes.guess_extension(file.content_type)
    filename = str(uuid.uuid1()) + extension
    AwsClient.upload_fileobj(file.stream, BucketName, filename)
    return filename

def download_image(filename):
    response = AwsClient.get_object(Bucket=BucketName, Key=filename)
    content_type = mimetypes.guess_type(filename)[0] or "image/jpeg"
    return response["Body"].read(), content_type
