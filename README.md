# django-elasticsearch
Demonstration for ElasticSearch intergration with Django.

### Run migrations
! python manage.py makemigrations <br>
! python manage.py migrate

### Populate DB using custom management commands
! python manage.py load_csv employers.csv<br>
or<br>
! python manage.py loaddata employers.json<br>
<i>This data comes from https://www.kaggle.com/datasets/kwongmeiki/forbes-the-global-2000-rankings-2023</i>

### Build indices for ElasticSearch
! python manage.py search_index --rebuild

### Run development server
! python manage.py runserver

