# urls.py
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Importe suas views

urlpatterns = [
    # ... suas outras URLs
    path('tinymce/', include('tinymce.urls')),
    path('upload-file/', views.upload_file, name='upload_file'),  # Rota para o upload
]

# Serve arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)