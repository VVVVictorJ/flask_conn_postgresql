#### 功能

flask 连接 potsgresql  
postgresql 数据库迁移
注册模块 register_func
登录模块 login

#### 目录结构

```
db-test/
├── app.py 	               服务器
├── config
│   ├── __init__.py
│   └── default.py         常规配置（debug，DATABASE_URI）
├── instance               隐私配置文件（api密钥之类的）
│   └── config.py
├── manage.py              迁移脚本
├── migrations
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── myapp
│   ├── __init__.py
│   └── models.py          数据库表
└── run.sh
```
