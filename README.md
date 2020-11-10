Mini Wallet Exercise
===

A simple wallet django app.

### Usage

To use the Wallet APIs, follow these steps:

1.Create a virtual environment (python -m venv bgVenv)
2.Follow the below steps to activate the virtual environment and install the packages mentioned 
```shell
Path>bgVenv\Scripts\activate
(bgVenv) D:\ws>pip install django
(bgVenv) D:\ws>pip install djangorestframework
(bgVenv) D:\ws>pip install downloadpath\mysqlclient-1.4.6-cp38-cp38-win32.whl
#Download link : https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
```

3.Add rest_framework,rest_framework.authtoken and restapiapp to INSTALLED_APPS

```shell
INSTALLED_APPS = [
 ...
 'rest_framework',
 'rest_framework.authtoken',
 'restapiapp'
]
```

4.Add the application's urls to your urlconf

```shell
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('api/v1/', include('restapiapp.urls'))
]
```

5.Apply migrations:

```python
(bgVenv) D:\ws>python manage.py makemigrations
(bgVenv) D:\ws>python manage.py migrate
```

### POST Enable my wallet

```python
http://localhost/api/v1/wallet
# HEADERS
Authorization  Token 6b3f7dc70abe8aed3e56658b86fa508b472bf238
```

### GET View my wallet balance

```python
http://localhost/api/v1/wallet
# HEADERS
Authorization  Token 6b3f7dc70abe8aed3e56658b86fa508b472bf238
```

### POST Add virtual money to my wallet

```python
http://localhost/api/v1/wallet/deposits
# HEADERS
Authorization  Token 6b3f7dc70abe8aed3e56658b86fa508b472bf238

# BODY formdata
amount         100000
reference_id   50535246-dcb2-4929-8cc9-004ea06f5241
```

### POST Use virtual money from my wallet

```python
http://localhost/api/v1/wallet/withdrawals
# HEADERS
Authorization  Token 6b3f7dc70abe8aed3e56658b86fa508b472bf238

# BODY formdata
amount         60000
reference_id   4b01c9bb-3acd-47dc-87db-d9ac483d20b2
```

### PATCH Disable my wallet

```python
http://localhost/api/v1/wallet
# HEADERS
Authorization  Token 6b3f7dc70abe8aed3e56658b86fa508b472bf238

# BODY formdata
is_disabled    true
```


### POST Initialize my account for wallet

```python
http://localhost/api/v1/init

# BODY formdata
customer_xid   ea0212d3-abd6-406f-8c67-868e814a2436
```
