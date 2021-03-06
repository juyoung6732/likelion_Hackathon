"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
import myapp.views
import api_test.urls

from django.conf.urls.static import static
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin', myapp.views.signin, name = 'signin'),
    path('signup', myapp.views.signup, name = 'signup'),
    path('', myapp.views.main, name = 'main'),
    path('myportfolio', myapp.views.myportfolio, name = 'myportfolio'),
    path('create', myapp.views.create, name = 'create'),
    path('kakaoproduct', myapp.views.kakaoproduct, name = 'kakaoproduct'),
    path('camera', myapp.views.camera, name='camera'),
    path('captureimage', myapp.views.captureimage, name='captureimage'),
    path('', include('django.contrib.auth.urls')),
    path('cameratest/', include('api_test.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
