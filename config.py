import boto3
from dotenv import load_dotenv

load_dotenv()

import os


class SystemConfig:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}".format(
            **{
                "user": os.getenv("SUPABASE_DB_USER"),
                "password": os.getenv("SUPABASE_DB_PASSWORD"),
                "host": os.getenv("SUPABASE_DB_HOST"),
                "port": os.getenv("SUPABASE_DB_PORT"),
                "db_name": os.getenv("SUPABASE_DB_NAME"),
            }
        )
    )


Config = SystemConfig

AwsClient = boto3.client("s3")
BucketName = "pastgram"
