- Install python and venv
- Criar virtual VENV no projeto "python -m venv venv"
- Ativar o ambiente virtual "source venv/bin/activate"
- Instalar o Django "pip install django"
- Iniciar o Projeto Django "django-admin startproject config ."
- Criar tabelas no banco "python manage.py migrate"
- Criar nosso super usuário "python manage.py createsuperuser"
- Rodar o servidor "python manage.py runserver"
- Acessar o admin Django "http://127.0.0.1:8000/admin/login/?next=/admin/"
- Criar um app Empresas "python manage.py startapp empresas"
- Configurar app empresas no config/settings.py "INSTALLED_APPS"
- Desenvolver no empresas/models.py a tabela do app empresa
- Executar o makemigration para criar o model do empresas "python manage.py makemigrations"
- Executar o migrate para criar tabelas no banco "python manage.py migrate"
- Registrar o app no arquivo admin 
- Criar o app funcionário "python manage.py startapp funcionarios"
- Criar tabela no models.py
- Registrar o Model no admin.py
- Executar o makemigration para criar o model do funcionário "python manage.py makemigration
- Criar tabela no banco "python manage.py migrate"
- Criar o app departamentos "python manage.py startapp departamentos"
- Criar tabela no models.py
- Registrar o Model no admin.py
- Executar o makemigration para criar o model do departamento "python manage.py makemigration
- Criar tabela no banco "python manage.py migrate"
- Criar o app documentos "python manage.py startapp documentos"
- Criar tabela no models.py
- Registrar o Model no admin.py
- Executar o makemigration para criar o model do documentos "python manage.py makemigration
- Criar tabela no banco "python manage.py migrate"
- Criar o app registro_hora_extra "python manage.py startapp registro_hora_extra"
- Criar tabela no models.py
- Registrar o Model no admin.py
- Executar o makemigration para criar o model do registro_hora_extra "python manage.py makemigration
- Criar tabela no banco "python manage.py migrate"
- Configurar no arquivo settings.py o template para o projeto 
- Criar Pasta template na raiz do projeto
- Configurar LANGUAGE_CODE e TIME_ZONE no arquivo settings.py
- Criar um arquivo base.html na pasta templates
- Configurar nossas urls do funcionario no arquivo config/urls.py
- Adicionar arquivo urls.py na pasta apps/funcionários
- Criar View de Funcionários do arquivo apps/funcionarios/views.py
- Criar App Core "python manage.py startapp core"
- Adicionar arquivo urls.py na pasta core
- Implementar view do core no arquivo views.py
- Criar template index.html na pasta core/templates
- Fazer download do Bootstrap e colocar pasta css e js na pasta static/bootstrap na raiz
- Adicionar no settings onde esta nossos arquivos css com STATICFILES_DIRS
- Carregar Boostrap no template base.html
- Envolver nosso block main em uma div container
- Adicionar no arquivo urls.py url para realizar login
- Criar Arquivo login.html na pasta templates/registration
- Definir no settings.py onde iremos mandar quando fizer o login utilizando LOGIN_REDIRECT_URL
- Criar a url home no arquivo apps/core/urls.py
- Forçar no index.html do core que o usuário esteja logado
- Configurar no settings.py onde queremos mandar o usuário após logout LOGOUT_REDIDERCT_URL