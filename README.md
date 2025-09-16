# fn-server
FastAPI server backend for nextjs .



## 测试

```shell

# 执行命令
pytest

```



## 配置



```bash
# 生成一个256位的AES密钥（这是最常见的密钥长度）：
openssl rand -base64 32
```



```bash
# 初始化
alembic init alembic
# 生成版本文件
alembic revision --autogenerate -m "Create initial tables"
# 执行迁移命令
alembic upgrade head
```
