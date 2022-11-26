### Django ile İHA Kiralama Projesi(Task)
---------------
Kullanılan Teknolojiler 
1. Python
2. Django
3. Nginx
4. Gunicorn
5. Postgresql
6. Docker
### Kurulum
--------------
**docker-compose.yml** dosyasıyla aynı dizindeyken aşagıdaki komutu çalıştırın.

    $ docker-compose up -d

docker çıktısında database migrateninin oldugundan emin olun aşagıdaki çıktı gibi olmalıdır.

    $ Running migrations:
    |  Applying contenttypes.0001_initial... OK
    |   Applying auth.0001_initial... OK
    |   Applying admin.0001_initial... OK
    |   Applying admin.0002_logentry_remove_auto_add... OK
    |   Applying admin.0003_logentry_add_action_flag_choices... OK
    |   Applying contenttypes.0002_remove_content_type_name... OK
    |   Applying auth.0002_alter_permission_name_max_length... OK
    |   Applying auth.0003_alter_user_email_max_length... OK
    |   Applying auth.0004_alter_user_username_opts... OK
    |   Applying auth.0005_alter_user_last_login_null... OK
    |   Applying auth.0006_require_contenttypes_0002... OK
    |   Applying auth.0007_alter_validators_add_error_messages... OK
    |   Applying auth.0008_alter_user_username_max_length... OK
    |   Applying auth.0009_alter_user_last_name_max_length... OK
    |   Applying auth.0010_alter_group_name_max_length... OK
    |   Applying auth.0011_update_proxy_permissions... OK
    |   Applying auth.0012_alter_user_first_name_max_length... OK
    |   Applying iha_app.0001_initial... OK
    |   Applying sessions.0001_initial... OK
    |   Applying user_app.0001_initial... OK
----------
Gerekli kurulumlar yapıldıktan sonra **http://0.0.0.0:8080/user/login/?next=/** adresini tarayıcıdan açın. Giriş sayfası açılacaktır. Önce hesap oluştur kısmından hesap oluşturup siteyi kullanmaya başlayabilirsiniz.


### Docker Olmadan Kurulum
-----------------
IHA/setting.py dosyasından

    $  DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'baykar',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            #'HOST': 'localhost',
            'HOST': 'db', # for docker
            'PORT': '5432',
        }
    }
gerekli ayarlamayı yapın.

    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
Komutlarıyla **localhost:8000** adresinden web sayfasını açın ve kullanmaya başlayın.

