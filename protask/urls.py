from django.contrib import admin
from django.urls import path, include
from todolist import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('list/', include('todolist.urls')),
    path('account/', include('users_app.urls')),
    path('contact-us', views.contact, name='contact'),
    path('abour-us', views.about, name='about'),
]
