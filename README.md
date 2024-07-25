# CALCULATOR

Este repositorio possui uma aplicação de calculadora simples, que realizar operações matemáticas básicas, ou seja, adição, subtração, multiplicação, divisão. 
Ela também pode calcular as raízes quadradas e a potência de um número.

## Requisitos

<div>
  <img src="https://img.shields.io/badge/Python-F4D03F?style=for-the-badge&amp;logo=Python&amp;logoColor=black" alt="PYTHON">
  <img src="https://img.shields.io/badge/Flask-323330?style=for-the-badge&amp;logo=Flask&amp;logoColor=white" alt="FLASK">
</div>

## Instalação

Todas as instalações abaixo são referentes ao Ubuntu

### Instalar Python

O Python geralmente já está instalado no Ubuntu, mas você pode verificar a versão digitando:

    $ python3 --version

Se não estiver instalado ou você precisar de uma versão específica, você pode instalar usando o apt:

    $ sudo apt update
    $ sudo apt install python3 python3-pip

### Instalar Flask

O Flask é um framework web em Python. Você pode instalar o Flask usando o `pip`, que é o gerenciador de pacotes do Python:

Primeiro deve-se criar um ambiente virtual (recomendado para isolar dependências do projeto):
    
    $ sudo apt install python3-venv
    $ python3 -m venv meuambiente
    $ source meuambiente/bin/activate

Agora instale o Flask dentro do ambiente virtual:

    $ pip install flask

Para verificar a versão instalada do Flask:

    $ python -m flask --version

## Uso

Após todas as dependencias instaladas, entre no diretorio Application via terminal

    $ cd Calculator/

E depois execute o comando

    $ python3 app.py

tendo executado o comando acima, abra o navegador de sua preferência e digite na barra de endereços: 

    http://localhost:5000

## Status do Projeto

**Status do Projeto: Concluído**

O projeto está funcional.

**Conquistas Atuais:**
- Funcionalidades básicas implementadas com sucesso.
- Backend e Frontend integrados.
- Estrutura de diretórios organizada e funcional.
- Interface do usuário (UI) está operacional.

**Próximos Passos:**
- Ajustar detalhes de layout e estilização.
- Implementar recursos adicionais.
- Melhorar a usabilidade e experiência do usuário.
- Realizar testes e correções de bugs.

O projeto encontra-se concluido.