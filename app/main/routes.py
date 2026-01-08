from flask import Blueprint, render_template, request, redirect, session
from app.models import Product

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # 임시 로그인 (DB 전)
        session["user"] = username
        session["role"] = "user"

        return redirect("/")

    return render_template("login.html")

@main_bp.route("/products")
def products():
    items = Product.query.all()
    return render_template("products.html", products=items)
