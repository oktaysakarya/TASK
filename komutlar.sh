
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
echo "** ----------------------------------------- **"
echo "** ----------------------------------------- **"
echo "** http://0.0.0.0:8080 adresini ziyaret edin **"
echo "** ----------------------------------------- **"
echo "** ----------------------------------------- **"
gunicorn IHA.wsgi:application --bind 0.0.0.0:8000
