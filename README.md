README.MD template:
```
https://gist.github.com/PurpleBooth/109311bb0361f32d87a2#file-readme-template-md
```

# DjangoSampleProject

Just not to start with empty one. 

### including
* Django-Bootstrap 3 powered
* Common project structure
* Built in registration
* List and detail views 

## Getting Started
```
virtualenv -p python3.6 venv
. venv/bin/activate
pip install -r requirements.txt
```
### Changing names

Project names changing: 

settings.py

```
INSTALLED APPS = [
    'newappname'
]
...
...
...
ROOT_URLCONF = 'NewProjectName.urls'
WSGI_APPLICATION = 'NewProjectName.wsgi.application'
```

wsgi.py

```
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewProjectName.settings")
```

manage.py

```
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewProjectName.settings")
```


apps.py

```
class NewAppNameConfig(AppConfig):
    name = 'newappname'
```


Change model and view names to those of your own.

Change template tags respectively, e.g:
 
```
{# url 'sampleapp:sampleview' #} to {% url 'yourapp:view' %}
```
