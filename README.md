"Code along from "Learn Full stack development with Django and react" by Hitesh Choudhary on Udemy. All rights belong to the original creators."

# 🛠️ Django + DRF Starter Project (Modular API with Pipenv)

A scalable Django + Django REST Framework (DRF) boilerplate for building modular API-based projects. Includes CORS support, media file handling, and a clean multi-app structure.

---

## 📦 Tech Stack

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [django-cors-headers](https://pypi.org/project/django-cors-headers/)
- [pipenv](https://pipenv.pypa.io/en/latest/)

---

## ⚙️ Getting Started

### 1. Clone the Repo & Set Up Environment

```bash
git clone https://github.com/ronnin796/ECOM.git
cd ECOM
## Start from here after 
pipenv install django djangorestframework django-cors-headers djangorestframework-simplejwt
pipenv shell

or start yourself 

2. Start Project & Apps

    create a folder then inside it install "djangorestframework django-cors-headers djangorestframework-simplejwt" //note: Use pipenv if using pipenv shell instead of just pip 
    django-admin startproject ECOM .
    cd ECOM
    django-admin startapp api
    cd api
    django-admin startapp category  # example app

3. Migrations & Superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

4. Update settings.py
INSTALLED_APPS = [
    ...
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'api',
]

NOTE!!!!!:- if you have featured apps inside you need to install using this structure
 'api.category',
    'api.product',
 and in the api/app_name/apps.py set name = "api.app_name" as it requires the full root path as its name to recognize

 see the documentations for the middleware and djang_rest settings 

 //my settings so far
 ##middleware
 MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]
####cors and media 

CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['*']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

###Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

## URL Configuration
##ECOM/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

##api/urls.py
from django.urls import path, include

urlpatterns = [
    path('category/', include('api.category.urls')),
]


####Feature App Setup: category

##models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

##admin.py
from django.contrib import admin
from .models import Category

admin.site.register(Category)


#serializers.py
from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

        NOTE!!!!!!:- If u want to serialize images u need 
        image = serializers.ImageField(max_length=None,allow_empty_file=False,allow_null=True,required=False) for image urls
        then put image in the "fields" attributes

##views.py

from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


##urls.py
from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet

router = routers.DefaultRouter()
router.register(r'', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



###Folder Structure

ECOM/
│
├── api/
│   ├── __init__.py
│   ├── urls.py
│   ├── category/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── admin.py
│   └── ...
│
├── ECOM/
│   └── settings.py
├── manage.py
└── Pipfile



##RUN THE SERVER
python manage.py runserver

Access API: http://127.0.0.1:8000/api/category/
Admin Panel: http://127.0.0.1:8000/admin/


Use Postman or curl to test endpoints.

Or browse endpoints via DRF’s UI (/api/category/).# ECOM
