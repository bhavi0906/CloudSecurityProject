from flask import render_template, request, redirect, flash, Blueprint
from services.blob_storage import upload_file

storage = Blueprint("storage", __name__)

@storage.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files.get("file")

        if file and file.filename != "":
            upload_file(file)
            flash("File uploaded successfully to Azure Blob Storage!")
            return redirect("/upload")

        flash("Please select a file.")

    return render_template("upload.html")