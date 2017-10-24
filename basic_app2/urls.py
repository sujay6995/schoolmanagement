from django.conf.urls import url
from basic_app2 import views

app_name ='basic_app2'

urlpatterns = [
        url(r'^createStudent/$',views.StudentCreateView.as_view(),name='create'),
        url(r'^delete/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='delete')
        ]