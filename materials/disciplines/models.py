# models.py
from django.db import models
from tinymce.models import HTMLField  # ou RichTextUploadingField do CKEditor

TIPO_NIVEL = {
    "PROEJA": "Proeja",
    "MEDIO": "Médio",
    "SUPERIOR": "Superior",
}

class Nivel(models.Model):
    nome = models.CharField(max_length=100, choices=TIPO_NIVEL.items())
    
    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=500)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Conteudo(models.Model):
    # Substituído TextField por HTMLField para ter o editor
    titulo        = models.CharField(max_length=500, default="Novo Conteúdo")
    descricao = models.TextField(max_length=1000000000000)  
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.disciplina.nome} - {self.titulo}"

class Atividades(models.Model):
    # Substituído TextField por HTMLField para ter o editor
    descricao = HTMLField(max_length=100)  
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE)

    def __str__(self):
        # Corrigido erro de sintaxe
        return f"{self.conteudo.titulo} - {self.descricao[:50]}"