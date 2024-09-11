from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name='login'),
    path('register/', views.signup, name='signup'),
    path('logout/', views.logout, name="logout"),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
    path('update/<int:pk>/', views.update_note, name='update_note')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)