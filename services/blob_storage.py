import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from werkzeug.utils import secure_filename

load_dotenv()

# Local development
CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# Running on Azure App Service
if os.getenv("WEBSITE_SITE_NAME"):
    credential = DefaultAzureCredential()

    client = SecretClient(
        vault_url="https://bhavyansh-keyvault.vault.azure.net/",
        credential=credential
    )

    CONNECTION_STRING = client.get_secret(
        "AZURE-STORAGE-CONNECTION-STRING"
    ).value

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