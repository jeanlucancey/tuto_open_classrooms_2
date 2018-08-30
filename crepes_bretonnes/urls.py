from django.contrib import admin
from django.urls import path, include

# Les deux lignes qui suivent, c'est pour gerer l'affichage de photos
from django.conf.urls.static import static
from django.conf import settings

from blog import views
from mini_url import views as views_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('mini_url/', include('mini_url.urls')),
    path('bloblo/<int:nombre1>', views.afficher_article, name='afficher_article'),
    path('todito/', views.todito, name='todito'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
