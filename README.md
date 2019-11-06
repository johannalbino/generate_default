# Gerando Arquivo Padrão (.sh)

### Problema identificado:

Para buscar dados no servidor linux eu precisava executar vários comandos do tipo:
rar a caminho/caminho/programa* # comentario

Gerando assim um arquivo rar com todas os arquivos indexados do cobol para assim realizar os testes internos.

Tinha a opção de criar manualmente um arquivo na extensão .sh e executar com o comando sh no caminho base do linux (/u), mas esse arquivo tinha que ser atualizado toda vez que tinha que executar pois tinha que alterar mês e ano das linhas.

### Solução:

Criar um site web com Django e Python para gerar um arquivo com extensão .sh de acordo com as definições que foram definidas no formulário (nome do cliente, departamento/setor, mes e ano) para rodar no servidor linux para buscar base de dados de acordo com os programas definidos e cadastrados no sistema.


# Intruções:

As bibliotecas utilizadas no desenvolvimento do projeto está no arquivo requirements.txt, para instalar só executar:

	pip install -r requirements.txt

Para criar o banco de dados deve executar:

	python manage.py makemigrations home
	python manage.py migrate
	python manage.py createsuperuser    #Para acessar a parte admin do django

Executar o programa localmente:

	python manage.py runserver localhost:8000  # A porta default é 8000, mas se quiser pode alterar para a desejada.

Só brincar no navegador e experimentar o programa.



