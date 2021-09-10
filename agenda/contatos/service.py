from .models import ContatoModel

def buscar_todos_contatos():
    return ContatoModel.objects.all()

def buscar_contato_by_id(id):
    return ContatoModel.objects.filter(id=id).first()