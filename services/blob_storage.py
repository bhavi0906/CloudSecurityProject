from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from werkzeug.utils import secure_filename
import os

# Load .env only for local development
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# First try local .env
CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

# If not found, fetch from Azure Key Vault
if not CONNECTION_STRING:
    KEYVAULT_NAME = "bhavyansh-keyvault"
    KV_URI = f"https://{KEYVAULT_NAME}.vault.azure.net/"

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KV_URI, credential=credential)

    CONNECTION_STRING = client.get_secret(
        "AZURE-STORAGE-CONNECTION-STRING"
    ).value

CONTAINER_NAME = "uploads"

blob_service_client = BlobServiceClient.from_connection_string(
    CONNECTION_STRING
)

def upload_file(file):
    filename = secure_filename(file.filename)

    blob_client = blob_service_client.get_blob_client(
        container=CONTAINER_NAME,
        blob=filename
    )

    blob_client.upload_blob(file, overwrite=True)

    return filename