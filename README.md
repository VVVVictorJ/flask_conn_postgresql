#### 功能

flask 连接 potsgresql  
postgresql 数据库迁移

#### 目录结构

db-test/
├── __pycache__
│   └── app.cpython-37.pyc
├── app.py 	               服务器
├── config
│   ├── __init__.py
│   ├── __pycache__
│   └── default.py         常规配置（debug，DATABASE_URI）
├── instance               隐私配置文件（api密钥之类的）
│   └── config.py
├── manage.py              迁移脚本
├── migrations
│   ├── README
│   ├── __pycache__
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── myapp
│   ├── __init__.py
│   ├── __pycache__
│   └── models.py          数据库表
└── run.sh
