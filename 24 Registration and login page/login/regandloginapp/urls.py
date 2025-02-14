from django.conf.urls import url
from . import views
app_name = 'regandloginapp'

urlpatterns = [
    path('$', views.home, name = 'home'),
    path('reg', views.reg, name = 'reg'),
    path('login', views.login, name = 'login'),
]