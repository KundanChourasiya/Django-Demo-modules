from django.conf.urls import url
from genericviews import views
app_name = 'genericviews'

urlpatterns = [
    path('', views.Indexview.as_view(), name='index'),
    path('(?<pk>[0-9]+)/',views.Detailsview.as_view(), name='details'),
    path('makeentry',views.makeentry.as_view(), name='makeentery'),
]