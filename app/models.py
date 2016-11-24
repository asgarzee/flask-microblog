from hashlib import md5

from app import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % self.nickname

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)

    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname=nickname).first() is None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname=new_nickname).first() is None:
                break
            version += 1
        return new_nickname


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % self.body


from sqlalchemy import event
import requests
import json


# standard decorator style
@event.listens_for(User, 'after_update')
def receive_after_update(mapper, connection, target):
    "listen for the 'after_update' event"
    data = {
        'nickname': target.nickname,
        'about me': target.about_me
    }
    response = requests.post(url=app.config.get('TARGET_URL', ''), data=json.dumps(data),
                             headers={"Content-Type": "application/json"})
    return


@event.listens_for(User, 'after_delete')
def receive_after_delete(mapper, connection, target):
    "listen for the 'after_delete' event"
    data = {
        'nickname': target.nickname,
        'about me': target.about_me
    }
    response = requests.post(url=app.config.get('TARGET_URL', ''), data=json.dumps(data),
                             headers={"Content-Type": "application/json"})
    return


@event.listens_for(User, 'after_insert')
def receive_after_insert(mapper, connection, target):
    "listen for the 'after_insert' event"
    data = {
        'nickname': target.nickname,
        'about me': target.about_me
    }
    response = requests.post(url=app.config.get('TARGET_URL', ''), data=json.dumps(data),
                             headers={"Content-Type": "application/json"})
    return
