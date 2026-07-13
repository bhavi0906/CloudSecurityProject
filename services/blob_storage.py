# deployment tetst - july 13
from azure.storage.blob import BlobServiceClient
from werkzeug.utils import secure_filename
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "uploads"

blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

def upload_file(file):
    filename = secure_filename(file.filename)

    blob_client = blob_service_client.get_blob_client(
        container=CONTAINER_NAME,
        blob=filename
    )

    blob_client.upload_blob(file, overwrite=True)

    return filename