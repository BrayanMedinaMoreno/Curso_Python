"""
from flask import Blueprint, request
import requests import get


user_github = Blueprint("users_github", __name__)

@user_github.route("/github/users", methods=["POST"])
def github():
    data = request.get()
    country = data["country"]
    return get
"""