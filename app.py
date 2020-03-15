from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config.default import Config
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__,instance_relative_config=True) 
#instance里的config通常存放api密钥等不想让人知道的配置
app.config.from_object(Config())
#调用的是当前根目录下的config文件
#此时根目录下没有config文件就不需要这句
#app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
"""
要注意每次启动服务器前都要添加DATABASE_URI环境变量，
打错一个I看了半小时
"""
#app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 
db = SQLAlchemy(app)
#engine = create_engine('postgresql://flask_server:zhj12345@localhost/videocommunity')
#Session = sessionmaker(bind=engine)
#session = Session()
#不需要上面这三行db是由flask_sqlalchemy中的SQLAlchemy注册的，db.session就可以使用会话

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(64))

    def __init__(self,email,username,password_hash):
        self.email = email
        self.username = username
        self.password_hash = password_hash

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def hello():
    return "Hello"

@app.route('/call',methods=['POST'])
def call_test():
    value = request.form['test']
    print("key's value is {}".format(value))
    return jsonify({
        "key":"value"
        })

@app.route('/register',methods=['POST'])
def register_func():
    booked = User.query.filter_by(username = request.form['username']).all()
    if booked.__len__() is not 0:
        return '0'
    username = request.form['username']
    password_hash = request.form['password_hash']
    mail = request.form['email']
    userinfo = User(username = request.form['username'], 
            password_hash = request.form['password_hash'],
            email = request.form['email'])
    db.session.add(userinfo)
    db.session.commit()
    return "success"

@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    registered = User.query.filter_by(username=request.form['username']).all()
    if registered.__len__() is not 0:
        passwd_right = User.query.filter_by(username=request.form['username'],
                password_hash=request.form['password_hash']).all()
        if passwd_right.__len__() is not 0:
            print(str(username)+" log success")
            return jsonify({
                username:"success"
                })
        else:
            print(str(username) + " log failed")
            return jsonify({
                username:"failed"
                })
    else:
        print(str(username)+" log failed")                                                      
        return jsonify({
            username:"try again"
            })

if __name__=='__main__':
    app.run()


