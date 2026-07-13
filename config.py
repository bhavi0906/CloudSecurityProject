import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from urllib.parse import quote_plus

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "cloudsecurityproject"

    # Local SQLite (fallback)
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        basedir, "database", "users.db"
    )

    # Running on Azure?
    if os.getenv("WEBSITE_SITE_NAME"):

        vault_url = "https://bhavyansh-keyvault.vault.azure.net/"

        credential = DefaultAzureCredential()

        client = SecretClient(
            vault_url=vault_url,
            credential=credential
        )

        conn = client.get_secret(
            "AZURE-SQL-CONNECTION-STRING"
        ).value

        
        

        SQLALCHEMY_DATABASE_URI = (
            "mssql+pyodbc:///?odbc_connect=" + quote_plus(conn)
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False