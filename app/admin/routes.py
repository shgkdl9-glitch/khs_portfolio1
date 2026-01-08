from flask import Blueprint, render_template, request, redirect, session, abort
from app.models import Product
from app import db

admin_bp = Blueprint("admin", __name__)

# 관리자 권한 체크
def admin_required():
    if session.get("role") != "admin":
        abort(403)

# 관리자 로그인
@admin_bp.route("/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        if (
            request.form.get("username") == "admin"
            and request.form.get("password") == "1234"
        ):
            session["role"] = "admin"
            return redirect("/admin/add-product")

    return render_template("admin_login.html")

# 상품 등록 (관리자 전용)
@admin_bp.route("/add-product", methods=["GET", "POST"])
def add_product():
    admin_required()

    if request.method == "POST":
        product = Product(
            name=request.form.get("name"),
            price=int(request.form.get("price")),
            description=request.form.get("description")
        )
        db.session.add(product)
        db.session.commit()
        return redirect("/products")

    return render_template("admin_add_product.html")
