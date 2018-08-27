from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('bloblo/<int:nombre1>', views.afficher_article, name='afficher_article'),
]
