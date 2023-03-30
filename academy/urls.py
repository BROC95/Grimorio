"""magic_academy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path


from grimorio.views import envio
from grimorio.views import grimorio
from grimorio.views import magos
from grimorio.views import delete
from grimorio.views import update
from grimorio.views import all
from grimorio.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('get/magos/', magos, name='magos'),
    path('get/grimorio/', grimorio, name='magos'),  # Metodos get
    path('all/', all, name='all'),  # Metodos post o patch
    path('post/', envio, name='envio'),
    path('update/', update, name='update'),
    path('del/', delete, name='del'),  # Metodo delete
]
