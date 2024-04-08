from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connections, DEFAULT_DB_ALIAS, OperationalError
from django.db.utils import DatabaseError


class Command(BaseCommand):
    help = '创建设置中指定的数据库（如果尚不存在）.'

    def add_arguments(self, parser):
        parser.add_argument('--database', default=DEFAULT_DB_ALIAS, help='指定要创建的数据库.')

    def handle(self, *args, **options):
        database_alias = options['database']
        db_options = settings.DATABASES.get(database_alias)

        if not db_options:
            self.stderr.write(self.style.ERROR(f"数据库别名 '{database_alias}' 未在设置中定义。数据库。"))
            return

        engine = db_options.get('ENGINE')
        database_name = db_options.get('NAME')

        if 'postgres' in engine:
            self.create_postgres_database(database_alias, database_name)
        else:
            self.stderr.write(self.style.ERROR(f"发动机 '{engine}' 此命令不支持。"))

    def create_postgres_database(self, alias, name):
        connection = connections[alias]

        # 断开与当前数据库的连接
        # 并连接到默认的“postgres”数据库
        connection.close()
        old_name = connection.settings_dict['NAME']
        connection.settings_dict['NAME'] = 'postgres'

        try:
            connection.ensure_connection()
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = %s", [name])
                exists = cursor.fetchone()
                if not exists:
                    cursor.execute(f"CREATE DATABASE {name}")
                    self.stdout.write(self.style.SUCCESS(f"已成功创建数据库 '{name}'."))
                else:
                    self.stdout.write(self.style.SUCCESS(f"数据库 '{name}' 已存在."))
        except OperationalError as e:
            self.stderr.write(self.style.ERROR(f"Operational error while creating database: {e}"))
        except DatabaseError as e:
            self.stderr.write(self.style.ERROR(f"Database error while creating database: {e}"))
        finally:
            # 还原旧数据库名称以重新建立原始连接
            connection.settings_dict['NAME'] = old_name
            connection.close()
