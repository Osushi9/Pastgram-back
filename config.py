import boto3
from dotenv import load_dotenv

load_dotenv()

import os


class SystemConfig:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8".format(
            **{
                "user": os.getenv("USER"),
                "password": os.getenv("PASSWORD"),
                "host": os.getenv("HOST"),
                "db_name": os.getenv("DB_NAME"),
            }
        )
    )


Config = SystemConfig

AwsClient = boto3.client("s3")
BucketName = "pastgram"
