from django.contrib import admin
from django.urls import path, include

# Les deux lignes qui suivent, c'est pour gerer l'affichage de photos
from django.conf.urls.static import static
from django.conf import settings

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('bloblo/<int:nombre1>', views.afficher_article, name='afficher_article'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
