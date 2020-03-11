from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from config.default import Config
import os

app = Flask(__name__,instance_relative_config=True) 
#instance里的config通常存放api密钥等不想让人知道的配置
app.config.from_object(Config())
#调用的是当前根目录下的config文件
#此时根目录下没有config文件就不需要这句
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI
#app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return "Hello"

if __name__=='__main__':
    app.run()


