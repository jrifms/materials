# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        # Salva o arquivo na pasta 'uploads' dentro de MEDIA_ROOT
        file_name = default_storage.save(f'uploads/{file.name}', ContentFile(file.read()))
        file_url = default_storage.url(file_name)
        
        # TinyMCE espera uma resposta JSON com a URL do arquivo
        return JsonResponse({'location': file_url})
    return JsonResponse({'error': 'Método não permitido'}, status=405)