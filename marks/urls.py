from django.conf.urls import url

from .import views

app_name = 'marks'

urlpatterns = [
    url(r'^home', views.home, name="home"),
    url(r'^teacher_login', views.teacher_login, name="teacher_login"),
    url(r'^upload', views.upload, name="upload"),
    url(r'^edit_marks', views.edit_marks, name="edit_marks"),
    url(r'^submit_marks', views.submit_marks, name="submit_marks"),
    url(r'^view_marks', views.view_marks, name="view_marks"),
    url(r'^logout', views.logout, name="logout")
]