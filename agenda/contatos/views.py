from django.shortcuts import render
from . import service
from rest_framework.views import APIView

class ContatosView(APIView):
    def get(self, request, contato_id=None):
        if contato_id != None:
            contato = service.buscar_contato_by_id(contato_id)
            return render(request, 'contatos.html', {'contato':contato})
        contatos = service.buscar_todos_contatos()
        return render(request, 'index.html', {'contatos':contatos})
