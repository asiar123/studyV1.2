"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include,url
from django.conf.urls.static import static
from django.conf import settings
from user.views import Login
from django.contrib.auth.views import logout_then_login
from matematicas.views import añadirMath
from biology.views import añadirBiology
from english.views import RegistroEnglish
from history.views import añadirHistory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('home.urls'))),
    path('accounts/login/', Login.as_view(), name = 'login'),
    url(r'^logout/', logout_then_login, name='logout'),
    path('user/',include(('user.urls','user'))),
    url(r'^person/', include ('person.urls')),
    path('math/',añadirMath.as_view(), name="matery"),
    path('biology/',añadirBiology.as_view(), name="biology"),
    path('english/',RegistroEnglish.as_view(), name="english"),
    path('history/',añadirHistory.as_view(), name="history"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
