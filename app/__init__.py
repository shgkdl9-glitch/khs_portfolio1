from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # =====================
    # 기본 설정
    # =====================
    app.config["SECRET_KEY"] = "secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # =====================
    # DB 초기화
    # =====================
    db.init_app(app)

    # =====================
    # Blueprint 등록
    # (순환 참조 방지)
    # =====================
    from app.main.routes import main_bp
    from app.admin.routes import admin_bp
    from app.payment.routes import payment_bp
    # from app.settlement.routes import settlement_bp  # 나중에

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(payment_bp)
    # app.register_blueprint(settlement_bp)

    # =====================
    # 개발용 테이블 생성
    # =====================
    with app.app_context():
        db.create_all()

    return app
