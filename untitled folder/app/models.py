from app.extensions import db
from flask_login import UserMixin


class Permission(db.Model):
    __tablename__ = 'permissions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    users = db.relationship('User', secondary='user_permissions', backref='permissions')

    def __repr__(self):
        return f"<Permission {self.name}>"


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    permissions = db.relationship('Permission', secondary='user_permissions', backref='users')

    def __repr__(self):
        return f"<User {self.username}>"


class UserPermissions(db.Model):
    __tablename__ = 'user_permissions'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'), primary_key=True)
