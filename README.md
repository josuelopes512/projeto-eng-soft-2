# projeto-eng-soft-2

#### Para migrate local
```python fastjobs/manage.py migrate```

#### Para migrate docker
```docker-compose exec web python manage.py migrate```

#### Para criar superuser local
```python fastjobs/manage.py createsuperuser```

#### Para criar superuser docker
```docker-compose exec web python manage.py createsuperuser```