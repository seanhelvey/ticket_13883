# ticket 13883

This contains minimal repro for (ticket 13883)[https://code.djangoproject.com/ticket/13883].


## Setup
```
# Run migrations.
./manage.py migrate

# Create an admin.
./manage.py createsuperuser
# admin, admin@dev.null, admin, admin, y

# Start server.
./manage.py runserver
```

Add several sports, some team, some not team.
http://127.0.0.1:8000/admin/demo/sport/add/


Visit http://127.0.0.1:8000/admin/demo/profile/add/.

The sports will be listed without grouping.

![Screen Shot 2021-07-19 at 8 45 22 AM](https://user-images.githubusercontent.com/1720010/126161864-08c587dc-0d37-4a58-af1d-6cf7e45f9de4.png)

