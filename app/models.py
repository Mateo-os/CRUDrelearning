from passlib.hash import bcrypt

from app.database import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self,password):
        self.password_hash = bcrypt.hash(password)
    
    def check_password(self, password):
        return bcrypt.verify(password, self.password_hash)

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(120),nullable = False)
    completed = db.Column(db.Boolean,default=False)

    def to_dict(self):
        return {
            "id":self.id,
            "title":self.title,
            "completed":self.completed
        }
    