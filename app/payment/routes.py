from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Order, Product
from app import db
import uuid

payment_bp = Blueprint(
    "payment",
    __name__,
    url_prefix="/payment"
)

@payment_bp.route("/create", methods=["POST"])
def create_order():
    # 1️⃣ 상품 ID 받기
    product_id = request.form.get("product_id")
    print("받은 product_id:", product_id)

    product = Product.query.get_or_404(product_id)

    # 2️⃣ 주문 생성
    order_uid = f"ORD_{uuid.uuid4().hex[:8]}"

    order = Order(
        order_uid=order_uid,
        buyer_id=1,              # TODO: 로그인 유저
        seller_id=product.seller_id,
        amount=product.price
    )

    db.session.add(order)
    db.session.commit()

    # 3️⃣ 결제 페이지로 이동
    return redirect(url_for("payment.pay_page", order_uid=order_uid))


@payment_bp.route("/pay/<order_uid>")
def pay_page(order_uid):
    order = Order.query.filter_by(order_uid=order_uid).first_or_404()

    return render_template(
        "payment.html",
        order=order
    )
