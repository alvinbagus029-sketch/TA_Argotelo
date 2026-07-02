import bcrypt

from flask import session

from Backend.model import db, User


class AuthService:

    @staticmethod
    def register(data):

        username = data.get("username")

        if User.query.filter_by(username=username).first():

            return {
                "success": False,
                "message": "Username sudah digunakan."
            }

        hashed_password = bcrypt.hashpw(
            data["password"].encode(),
            bcrypt.gensalt()
        ).decode()

        user = User(
            role_id=data["role_id"],
            fullname=data["fullname"],
            username=username,
            password=hashed_password,
            email=data.get("email"),
            phone=data.get("phone")
        )

        db.session.add(user)
        db.session.commit()

        return {
            "success": True,
            "message": "Registrasi berhasil."
        }


    @staticmethod
    def login(data):

        user = User.query.filter_by(
            username=data["username"]
        ).first()

        if not user:

            return {
                "success": False,
                "message": "Username tidak ditemukan."
            }

        if not bcrypt.checkpw(
            data["password"].encode(),
            user.password.encode()
        ):

            return {
                "success": False,
                "message": "Password salah."
            }

        session["user_id"] = user.id
        session["role_id"] = user.role_id
        session["fullname"] = user.fullname

        return {
            "success": True,
            "role_id": user.role_id,
            "fullname": user.fullname
        }


    @staticmethod
    def logout():

        session.clear()

        return {
            "success": True
        }


    @staticmethod
    def me():

        if "user_id" not in session:

            return {
                "success": False
            }

        return {
            "success": True,
            "user_id": session["user_id"],
            "role_id": session["role_id"],
            "fullname": session["fullname"]
        }