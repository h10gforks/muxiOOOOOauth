# coding: utf-8
"""
sql models

    use: Flask-SQLAlchemy
    -- http://flask-sqlalchemy.pocoo.org/2.1/

"""

from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin, current_user
from wtforms.validators import Email
from itsdangerous import URLSafeSerializer as Serializer
from rest.auth import AuthUser

# permissions
class Permission:
    """
    1. COMMENT: 0x01
    2. MODERATE_COMMENTS: 0x02
    3. ADMINISTER: 0x04
    """
    COMMENT = 0x01
    MODERATE_COMMENTS = 0x02
    ADMINISTER = 0x04


# user roles
class Role(db.Model):
    """
    1. User: COMMENT
    2. Moderator: MODERATE_COMMENTS
    3. Administrator: ADMINISTER
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.COMMENT, True),
            'Moderator': (Permission.COMMENT |
                          Permission.MODERATE_COMMENTS, False),
            'Administrator': (
                Permission.COMMENT |
                Permission.MODERATE_COMMENTS |
                Permission.ADMINISTER,
                False
            )
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model, UserMixin, AuthUser):
    """
    muxi~auth 用户模块
    开发者, 注册用户
    区别仅在于是否注册了应用
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(164), unique=True, index=True)
    email = db.Column(db.String(164), info={'validator' : Email()})
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(164))
    sid = db.Column(db.String(20))
    school = db.Column(db.String(164))
    phone = db.Column(db.String(20))
    qq = db.Column(db.String(20))
    clients = db.relationship('Client', backref="users", lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def is_admin(self):
        if self.role_id == 2:
            return True
        return False

    def to_json(self):
        json_user = {
            id = self.id,
            username = self.username,
            email = self.email,
            sid = self.sid,
            school = self.school,
            phone = self.phone,
            qq = self.qq
        }
        return json_user

    @staticmethod
    def from_json(json_user):
        user = User(
            username = json_user.get("username"),
            password = json_user.get("password"),
            email = json_user.get("email"),
            sid = json_user.get("sid", None)
            school = json_user.get("school", None)
            phone = json_user.get("phone", None)
            qq = json_user.get("qq", None)
        )
        db.session.add(user)
        db.session.commit()
        return user

    def __repr__(self):
        return "<User %r>" % self.username


class AnonymousUser(AnonymousUserMixin):
    """ anonymous user """
    def is_admin(self):
        return False

login_manager.anonymous_user = AnonymousUser

# you can writing your models here:
class Client(db.Model):
    """
    muxi~auth 第三方应用模块
    开发者注册第三方应用
    client_id, client_key
    利用id和key生成client_token(grant token)
    从而获取用户信息
    """
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(164), unique=True)
    client_key = db.Column(db.String(15)) # 10
    # developer id
    dev_id = db.Column(db.ForeignKey("users.id"))

    def generate_client_token(self):
        """
        use client_id & client_key
        to generate client grant token
        """
        s = Serializer(
            self.client_key
        )
        return s.dumps({'client_id': self.id})

    @staticmethod
    def verify_client_token(token):
        """
        verify client token
        but need client_key
        """
        s = Serializer(
            self.client_key
        )
        data = s.loads(token)
        return Client.query.get_or_404(data['id'])

    def __repr__(self):
        return "<client %r>" % self.name

