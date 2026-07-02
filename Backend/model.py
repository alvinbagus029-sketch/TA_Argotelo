from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# =====================================
# ROLE
# =====================================

class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(30), unique=True, nullable=False)

    users = db.relationship("User", backref="role", lazy=True)


# =====================================
# USER
# =====================================

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    role_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.id"),
        nullable=False
    )

    fullname = db.Column(
        db.String(100),
        nullable=False
    )

    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    email = db.Column(db.String(100))

    phone = db.Column(db.String(20))

    status = db.Column(
        db.Enum("Active", "Inactive"),
        default="Active"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    transactions = db.relationship(
        "Transaction",
        backref="cashier",
        lazy=True
    )

    attendance = db.relationship(
        "Attendance",
        backref="user",
        lazy=True
    )


# =====================================
# CATEGORY
# =====================================

class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)

    category_name = db.Column(
        db.String(100),
        nullable=False
    )

    menus = db.relationship(
        "Menu",
        backref="category",
        lazy=True
    )


# =====================================
# MENU
# =====================================

class Menu(db.Model):
    __tablename__ = "menus"

    id = db.Column(db.Integer, primary_key=True)

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id")
    )

    menu_name = db.Column(db.String(100))

    description = db.Column(db.Text)

    price = db.Column(db.Numeric(12,2))

    image_url = db.Column(db.Text)

    status = db.Column(
        db.Enum(
            "Available",
            "Unavailable"
        ),
        default="Available"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    transaction_details = db.relationship(
        "TransactionDetail",
        backref="menu",
        lazy=True
    )


# =====================================
# SUPPLIER
# =====================================

class Supplier(db.Model):
    __tablename__ = "suppliers"

    id = db.Column(db.Integer, primary_key=True)

    supplier_name = db.Column(db.String(100))

    phone = db.Column(db.String(20))

    address = db.Column(db.Text)

    inventories = db.relationship(
        "Inventory",
        backref="supplier",
        lazy=True
    )


# =====================================
# INVENTORY
# =====================================

class Inventory(db.Model):
    __tablename__ = "inventories"

    id = db.Column(db.Integer, primary_key=True)

    supplier_id = db.Column(
        db.Integer,
        db.ForeignKey("suppliers.id")
    )

    item_name = db.Column(db.String(100))

    unit = db.Column(db.String(30))

    stock = db.Column(db.Numeric(10,2))

    minimum_stock = db.Column(db.Numeric(10,2))

    stock_logs = db.relationship(
        "StockLog",
        backref="inventory",
        lazy=True
    )


# =====================================
# STOCK LOG
# =====================================

class StockLog(db.Model):
    __tablename__ = "stock_logs"

    id = db.Column(db.Integer, primary_key=True)

    inventory_id = db.Column(
        db.Integer,
        db.ForeignKey("inventories.id")
    )

    qty = db.Column(db.Numeric(10,2))

    type = db.Column(
        db.Enum(
            "IN",
            "OUT"
        )
    )

    note = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# =====================================
# TRANSACTION
# =====================================

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)

    invoice_number = db.Column(
        db.String(50),
        unique=True
    )

    cashier_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    subtotal = db.Column(db.Numeric(12,2))

    tax = db.Column(db.Numeric(12,2))

    total = db.Column(db.Numeric(12,2))

    payment_status = db.Column(
        db.Enum(
            "Pending",
            "Paid",
            "Cancelled"
        )
    )

    transaction_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    transaction_details = db.relationship(
        "TransactionDetail",
        backref="transaction",
        lazy=True
    )

    payments = db.relationship(
        "Payment",
        backref="transaction",
        lazy=True
    )


# =====================================
# TRANSACTION DETAIL
# =====================================

class TransactionDetail(db.Model):
    __tablename__ = "transaction_details"

    id = db.Column(db.Integer, primary_key=True)

    transaction_id = db.Column(
        db.Integer,
        db.ForeignKey("transactions.id")
    )

    menu_id = db.Column(
        db.Integer,
        db.ForeignKey("menus.id")
    )

    quantity = db.Column(db.Integer)

    price = db.Column(db.Numeric(12,2))

    subtotal = db.Column(db.Numeric(12,2))


# =====================================
# PAYMENT
# =====================================

class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)

    transaction_id = db.Column(
        db.Integer,
        db.ForeignKey("transactions.id")
    )

    payment_method = db.Column(db.String(50))

    midtrans_order_id = db.Column(db.String(100))

    midtrans_transaction_id = db.Column(db.String(100))

    payment_status = db.Column(db.String(50))

    paid_at = db.Column(db.DateTime)


# =====================================
# ATTENDANCE
# =====================================

class Attendance(db.Model):
    __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    check_in = db.Column(db.DateTime)

    check_out = db.Column(db.DateTime)

    status = db.Column(db.String(30))


# =====================================
# SHIFT
# =====================================

class Shift(db.Model):
    __tablename__ = "shifts"

    id = db.Column(db.Integer, primary_key=True)

    shift_name = db.Column(db.String(50))

    start_time = db.Column(db.Time)

    end_time = db.Column(db.Time)