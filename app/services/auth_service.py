from flask_jwt_extended import create_access_token

from app.database import db
from app.models import User

def register_user(username:str, password:str) -> User:
    user = User(username=username) #type: ignore
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return user

def authenticate_user(username: str, password: str):
    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return None
    token = create_access_token(identity=user.id)
    return token
