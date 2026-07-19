import os
import json
import boto3
from dotenv import load_dotenv

load_dotenv()


def get_database_config():

    # Production - Read from AWS Secrets Manager
    if os.getenv("ENVIRONMENT") == "production":

        client = boto3.client(
            "secretsmanager",
            region_name="ap-south-2"
        )

        response = client.get_secret_value(
            SecretId="bankapp/postgres"
        )

        secret = json.loads(response["SecretString"])

        return {
            "host": secret["host"],
            "database": secret["database"],
            "user": secret["username"],
            "password": secret["password"],
            "port": secret["port"]
        }

    # Development - Read from .env
    return {
        "host": os.getenv("DB_HOST"),
        "database": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "port": os.getenv("DB_PORT")
    }
