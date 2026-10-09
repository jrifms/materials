# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Conteudo

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


def listar_conteudos(request):
    """
    Lista todos os conteúdos cadastrados.
    """

    conteudos = Conteudo.objects.select_related(
        "disciplina",
        "disciplina__nivel"
    ).order_by(
        "disciplina__nome",
        "titulo"
    )

    return render(
        request,
        "disciplines/listar_conteudos.html",
        {
            "conteudos": conteudos
        }
    )

def visualizar_conteudo(request, conteudo_id):
    """
    Recupera o conteúdo e apresenta o HTML armazenado.
    """

    conteudo = get_object_or_404(
        Conteudo,
        pk=conteudo_id
    )

    # Retorna diretamente a página HTML armazenada.
    return HttpResponse(
        conteudo.descricao,
        content_type="text/html; charset=utf-8"
    )