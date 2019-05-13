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
virtualenv -p python3.6 venv
. venv/bin/activate
pip install -r requirements.txt

### Changing names
Change model and view names to those of your own.
Change template tags respectively, e.g:
 
```
{# url 'sampleapp:sampleview' #} to {% url 'yourapp:view' %}
```