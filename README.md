# Projeto: Gerenciador de Tarefas com Flask e Arquitetura MVC

## 📖 Descrição do Projeto

Este projeto consiste na evolução de uma API RESTful simples para uma aplicação web mais robusta, utilizando a arquitetura **MVC (Model-View-Controller)**. A aplicação, desenvolvida como atividade acadêmica, é um "Gerenciador de Tarefas" (To-Do List) construído com Python, Flask e SQLAlchemy para persistência de dados em um banco de dados SQLite.

O projeto partiu de uma API básica, disponível em [api-flask (versão inicial)](https://github.com/JoaoVictor2201/api-flask), e foi refatorado para seguir melhores práticas de desenvolvimento, separando as responsabilidades em camadas distintas e adicionando uma interface web para interação do usuário.

## ✨ Funcionalidades Principais

A aplicação permite o gerenciamento completo de Usuários e Tarefas associadas a eles, implementando um relacionamento de "um-para-muitos" (um usuário pode ter várias tarefas).

### Gerenciamento de Usuários
- **Listagem de Usuários:** Visualização de todos os usuários cadastrados no banco de dados.
- **Criação de Usuários:** Formulário para adicionar novos usuários ao sistema.

### Gerenciamento de Tarefas
- [cite_start]**Listagem de Tarefas:** Exibe todas as tarefas, mostrando seus detalhes como título, descrição, status e a qual usuário pertencem[cite: 50, 51].
- [cite_start]**Criação de Tarefa:** Formulário para adicionar uma nova tarefa e associá-la a um usuário existente através de um campo de seleção[cite: 54, 55].
- [cite_start]**Atualização de Status:** Permite alterar o status de uma tarefa entre 'Pendente' e 'Concluído' diretamente da lista[cite: 40, 52].
- [cite_start]**Exclusão de Tarefa:** Permite remover uma tarefa do banco de dados[cite: 44, 52].

## 🛠️ Tecnologias e Padrões Utilizados

- **Backend:** Python
- **Framework:** Flask
- [cite_start]**ORM:** SQLAlchemy [cite: 12]
- [cite_start]**Banco de Dados:** SQLite [cite: 12]
- [cite_start]**Arquitetura:** MVC (Model-View-Controller) [cite: 14]
- [cite_start]**Templates:** Jinja2 [cite: 12]
- **Estrutura do Projeto:** Padrão *Application Factory* e *Blueprints* para organização das rotas.

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e executar a aplicação em seu ambiente local.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/JoaoVictor2201/api-flask-MVC.git](https://github.com/JoaoVictor2201/api-flask-MVC.git)
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd api-flask-MVC
    ```

3.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente virtual
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

4.  **Instale as dependências do projeto:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute a aplicação:**
    ```bash
    python run.py
    ```
    [cite_start]Ao ser executada pela primeira vez, a aplicação criará automaticamente o arquivo de banco de dados `database.db` com as tabelas `users` e `tasks`[cite: 67].

6.  **Acesse a aplicação:**
    Abra seu navegador e acesse as seguintes URLs:
    - **Página de Usuários:** `http://127.0.0.1:5000/`
    - **Página de Tarefas:** `http://127.0.0.1:5000/tasks`

## 👨‍💻 Autor

**João Victor**