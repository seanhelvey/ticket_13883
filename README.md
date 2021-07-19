# ticket 13883

This contains minimal repro for [https://code.djangoproject.com/ticket/13883](ticket 13883).


## Setup
```
# Run migrations.
./manage.py migrate

# Create an admin.
./manage.py createsuperuser
# admin, admin@dev.null, admin is fine

# Start server.
./manage.py runserver
```


http://127.0.0.1:8000/admin/

