from flask import Blueprint, request, abort, jsonify, current_app, send_file
from os import listdir, path, remove

uploads = Blueprint('uploads', __name__, url_prefix="/uploads")

@uploads.route("/", methods=["GET"])
def upload_index():
    contents = listdir(current_app.config["UPLOAD_FOLDER"])
    files = [file for file in contents if file[0] != "."]
    return jsonify(files)

@uploads.route("/", methods=["POST"])
def upload_create():
    if "file" in request.files and request.files["file"].filename != "":
        file = request.files["file"]
        file.save(path.join(current_app.config["UPLOAD_FOLDER"], file.filename))
        return ("", 200)
    return abort(400)

@uploads.route("/<string:name>", methods=["GET"])
def upload_show(name):
    filepath = path.join(current_app.config["UPLOAD_FOLDER"], name)
    if path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    return abort(404)


@uploads.route("/<string:name>", methods=["DELETE"])
def upload_delete(name):
    filepath = path.join(current_app.config["UPLOAD_FOLDER"], name)
    if path.exists(filepath):
        remove(filepath)
        return ("", 200)
    return abort(404)