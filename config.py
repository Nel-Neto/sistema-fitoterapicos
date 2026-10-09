
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD", ""))
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "fitoterapicos")


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@"
        f"{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    if os.getenv("DB_SSL", "false").lower() == "true":
        SQLALCHEMY_ENGINE_OPTIONS = {
            "connect_args": {
                "ssl_ca": os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    "certs",
                    "ca.pem"
                ),
                "ssl_verify_cert": True,
                "ssl_verify_identity": True,
            }
        }