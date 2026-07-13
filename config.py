import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = "cloudsecurityproject"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Local development
    SQLALCHEMY_DATABASE_URI = os.getenv("AZURE_SQL_CONNECTION_STRING")

    # Running in Azure App Service
    if os.getenv("WEBSITE_SITE_NAME"):

        credential = DefaultAzureCredential()

        client = SecretClient(
            vault_url="https://bhavyansh-keyvault.vault.azure.net/",
            credential=credential
        )

        SQLALCHEMY_DATABASE_URI = client.get_secret(
            "AZURE-SQL-CONNECTION-STRING"
        ).value