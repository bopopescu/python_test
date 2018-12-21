# -*- coding: utf-8 -*-

# @Time    : 2018/12/4 16:58
# @Author  : songq001
# @Comment : 

from . import db
from flask_login import UserMixin, AnonymousUserMixin, current_user
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return OusiStaff.query.get(int(user_id))


class OusiStaff(UserMixin, db.Model):
    __tablename__ = 'ousi_staff'
    sid = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(8))
    name = db.Column(db.String(8))
    password = db.Column(db.String(8))
    phone = db.Column(db.String(11))
    role = db.Column(db.String(8))

    def is_admin(self):
        return self.role == 'admin'


class AnonymousUser(AnonymousUserMixin):
    def is_admin(self):
        return False


login_manager.anonymous_user = AnonymousUser


class OusiGuest(db.Model):
    __tablename__ = 'ousi_guest'
    id = db.Column(db.Integer, primary_key=True)
    staff_phone = db.Column(db.String(11))
    name = db.Column(db.String(8))
    month = db.Column(db.String(8))
    balance = db.Column(db.Integer)


