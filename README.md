# projeto-eng-soft-2

#### Para migrate local
```python fastjobs/manage.py migrate```

#### Para migrate docker
```docker-compose exec web python manage.py migrate```

#### Para criar superuser local
```python fastjobs/manage.py createsuperuser```

#### Para criar superuser docker
```docker-compose exec web python manage.py createsuperuser```

#### Para fazer os testes automatizados local
```python fastjobs/manage.py test```

#### Para fazer os testes automatizados docker
```docker-compose exec web python manage.py test```

#### Para acessar o python shell local
```python fastjobs/manage.py shell```

#### Para acessar o python shell docker
```docker-compose exec web python manage.py shell```

#### Para criar pasta static local
```python fastjobs/manage.py collectstatic --noinput```

#### Para criar pasta static docker
```docker-compose exec web python manage.py collectstatic --noinput```