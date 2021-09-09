# Como Construir Aplicação Django
## _Projeto Django para criação de Escola_


## Installation
Será necessário ter instalado em sua maquina a última versão do Python.

- Instalar na sua maquina a virtualenv. [Documentação](https://virtualenv.pypa.io/en/latest/installation.html)

```sh
python -m pip install --user virtualenv
python -m virtualenv --help
```


- Criar o ambiente virtual na pasta do seu projeto. Com esse comando, irá criar uma pasta na raiz do seu projeto chamada venv.
```sh
virtualenv venv -p python3.9
```

- Para ativar sua maquina virtual será preciso rodar o seguinte comando:
```sh
source venv/bin/activate
```

- Agora precisamos instalar o django na nossa maquina virtual, lembrando que precisamos ter o ambiente ativo, se não irá instalar na sua maquina local. Se você perceber, após a instalação na pasta venv/bin será instalado o django.
```sh
pip install django
pip install djangorestframework
```

## Development

Para você criar um projeto DJANGO igual a esse será necessário seguir os passos a seguir, nos passos anteriores de instalção, serve para você ter o ambiente na sua maquina para podermos desenvolver esse projeto.

- Para começarmos precisamos iniciar nosso projeto Django, isso sempre na raiz da pasta que você irá criar seu projeto. O seguinte comando irá criar uma pasta config, que estará todos os seus arquivos de de configuração do django. Também irá ser criado um arquivo manage.py, que seria o orquestrador do djagno, tods os comandos irá ser passado por ele. Emplicando um pouco melhor sobre os arquivos criados na pasta config, o arquivo url.py é reponsável pelas definições das urls do seu projeto. O arquivo settings.py é o arquivo mais importante do Django, responsável pelas configurações django.
```sh
django-admin startproject config .
```

- Agora iremos configurar nosso banco de dados. Primeiramente teremos que modificar o arquivo settings.py que se encontra na pasta config, precisamos importar a biblioteca os no começo do nosso arquivo `import os`. Na variável `DATABASES` é onde iremos configurar nosso banco de dados, por padrão django, já temos um banco configurado que seria o sqlite3.

- No mesmo arquivo settings.py temos no final do arquivo a variável `LANGUAGE_CODE` e `TIME_ZONE` que se refere com a linguagem do projeto e o timezone de onde esse projeto deve se espelhar, iremos modificar `LANGUAGE_CODE` da seguinte forma:
`LANGUAGE_CODE = 'pt-br'`

- Na variavel `INSTALLED_APPS` é onde iremos adicionar nossos apps que iremos criar, ou seja, nossa aplicação sempre passa por ali para identificar os apps, modelos e etc que serão utilizados, por padrão o django já vem com alguns apps deles instalados. Vamos fazer um teste, na sua linha de comando rode o seguinte comando:
```sh
python manage.py migrate
```
- Este comando serve para a criação de tabelas no nosso banco de dados, banco de dados que definimos da variável `DATABASES` que por padrão djago será utilizado o sqlite3. Podemos percerber também que algumas tabelas criadas se refere dos apps que definimos na variável `INSTALLED_APPS`, sim, o django utiliza essa variável para a criação do banco e outras coisas mais. Se você observar foi criado na raiz do projeto um arquivo chamado `db.sqlite3`, esse é o nosso arquivo do banco de dados.


- Agora iremos fazer a criação dos nossos apps do projeto. Para podermos criar um app, o django facilita nossa vida, basta utilizarmos o seguinte comando 
```sh
python manage.py startapp core
```
- Perceba que foi criado uma pasta(core) na raiz do seu projeto. Para organizamos nossa aplicação, vamos criar uma pasta na raiz do seu projeto chamada `apps`, iremos colocar todos os nossos apps nessa pasta, vamos colocar nossa pasta `core` nessa pasta, ficará da seguinte forma -> `apps/core`. Esse apps `core` utilizaremos para as coisas uteis do nosso projeto, isso depende muito de desenvolver por desenvolvedor.
- Com a nova atualização do django, com a versão 2, precisamos alterar em todos os nossos apps no arquivo `apps.py`, como estamos organizando tudo na pasta `apps` precisamos alterar no arquivo `apps.py` a variável `name` da seguinte forma:
> old: `name = 'core'` valor antigo da variável.
> new: `name = 'apps.core'` valor que teremos que alterar.


- Agora vamos registrar no app no nossa arquivo de configuração `settings.py` na variável `INSTALLED_APPS`, vamos adicionar `'apps.core',` no final do da lista.

- Explicando um pouco sobre os arquivos criados na pasta core, temos o arquivo `views.py`  é o arquivo responsável por capturar nossas requisições nas urls. No arquivo `models.py` é onde registramos nosso modelo do banco de dados, precisamos definir colunas e tudo mais que define o banco de dados, o django passa por esse arquivo para criar as tabelas no banco. Vamos criar um arquivo nessa pasta `core` chamado `url.py` que será responsável pelas urls desse nosso app.

- Agora vamos criar na pasta `core` uma pasta `templates`, essa pasta irá ficar nosso templates desse app, por padrão, o django já recohece essa pasta como pasta de templates. Vamos criar um arquivo chamado `home.html` nessa pasta templates.

- Vamos configurar nossos arquivos staticos, qur ficara em cada app chamado de `static` ele ficará responsável por armazenar nossos arquivos estaticos, como css e js. E precisamos também configurar onde o projeto irá pegar esses arquivos estaticos.
