from app import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), default="user")


class Product(db.Model):
    __tablename__ = "product"   # ⭐ 핵심

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_uid = db.Column(db.String(50), unique=True, nullable=False)

    buyer_id = db.Column(db.Integer, nullable=False)
    seller_id = db.Column(db.Integer, nullable=False)

    amount = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default="READY")
    created_at = db.Column(db.DateTime, default=db.func.now())

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_uid = db.Column(db.String(50), nullable=False)
    pg_tid = db.Column(db.String(100))  # PG 거래 ID

    paid_amount = db.Column(db.Integer)
    pay_method = db.Column(db.String(20))
    status = db.Column(db.String(20))  # PAID / FAILED

    paid_at = db.Column(db.DateTime)

class Settlement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_uid = db.Column(db.String(50), nullable=False)
    seller_id = db.Column(db.Integer, nullable=False)

    total_amount = db.Column(db.Integer)
    platform_fee = db.Column(db.Integer)
    payout_amount = db.Column(db.Integer)

    status = db.Column(db.String(20), default="WAITING")
    settled_at = db.Column(db.DateTime)
