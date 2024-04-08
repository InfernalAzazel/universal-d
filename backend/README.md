# 后端

默认支持 pgsql


### 步骤 1: 运行迁移

配置好设置后，运行 Django 的迁移命令来创建数据库模式：

```bash
python manage.py makemigrations
python manage.py migrate
```

这些命令将会创建所有由你的 `models.py` 文件定义的数据库表。

### 步骤 2: 创建超级用户（可选）

如果你希望使用 Django 的管理界面，可以创建一个超级用户：

```bash
python manage.py createsuperuser
```

按照提示输入所需的详细信息。

### 步骤 3: 测试连接

最后，运行你的 Django 开发服务器来测试数据库连接是否成功：

```bash
python manage.py runserver
```