# N3 Web

Este projeto é uma aplicação Flask demonstrando:

- **Internacionalização (i18n)** de todas as páginas (suporte a `pt_BR`, `en` e `es`).
- **Paginação** em ao menos duas páginas.
- **Bloqueio e liberação de rotas** com base em regras de permissão de usuários (usuários comuns vs. administradores).

## Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- Python 3.8+
- `pip` (gerenciador de pacotes do Python)

Também é recomendável a utilização de um ambiente virtual (*virtualenv*, *venv*, *conda*, etc.) para evitar conflitos de dependências.

## Instalação das Dependências

Crie e ative um ambiente virtual (opcional, mas recomendado):

Instale as dependências listadas no arquivo `requirements.txt`:


pip install -r requirements.txt


Executando a Aplicação

Com o ambiente virtual ativado e as dependências instaladas, inicie o servidor Flask:

python app.py
Acesse a aplicação em seu navegador no endereço:

http://127.0.0.1:5000


## Funcionalidades da Aplicação

Autenticação e Perfis de Usuário
A aplicação simula uma base de usuários com dois perfis:

Administrador (admin):
Usuário: admin
Senha: adminpass
Usuário Comum (user):
Usuário: user
Senha: userpass
Para acessar rotas protegidas, você precisará efetuar o login pela página de Login:

Página de Login: /login
Ao efetuar login como admin, você terá acesso às páginas administrativas e de consulta.

Ao efetuar login como user, você terá acesso apenas às páginas de consulta.

Bloqueio e Liberação de Rotas
Usuários comuns:

Têm acesso às páginas de consulta (exemplo: lista de usuários).
Não têm acesso a páginas administrativas.
Administradores:

Têm acesso às páginas de administração e também às de consulta.
Exemplos de Rotas:

Rota administrativa: /admin (acessível apenas para admin)
Rota de consulta: /users (acessível tanto para admin quanto para user após login)
Internacionalização (i18n)
A aplicação suporta três idiomas: pt_BR, en e es.

O idioma padrão é pt_BR. Para mudar o idioma, utilize os ícones de bandeira na navbar ou acesse a rota de mudança de idioma diretamente:

/change_language/pt_BR
/change_language/en
/change_language/es
As traduções encontram-se no diretório translations/.

## Paginação
A funcionalidade de paginação está implementada em ao menos duas páginas de listagem. Um exemplo é a página de usuários:

Rota: /users
Nesta página, você verá uma lista paginada de usuários. Através dos links de paginação, é possível navegar entre diferentes páginas de resultados.

## Testes Funcionais

Testar o Login e Proteção de Rotas:
Acesse a página /login.
Faça login como user:
Usuário: user
Senha: userpass

Verifique se consegue acessar /users (deve funcionar) e se não consegue acessar /admin (deve dar erro 403).

Faça logout e tente acessar rotas protegidas diretamente para confirmar se o redirecionamento para /login ocorre.

Em seguida, faça login como admin:

Usuário: admin
Senha: adminpass

Verifique o acesso à página /admin (deve funcionar) e também à /users.

Testar Internacionalização:

Use os links de idioma na navbar ou acesse:

/change_language/en
/change_language/es
/change_language/pt_BR

Confira se a interface (menus, títulos, textos) é exibida no idioma selecionado.

Testar Paginação:

Acesse /users.

Navegue pelas páginas através dos links de paginação.

Verifique se a lista de usuários muda conforme a página selecionada.

Todos esses testes podem ser executados manualmente pelo navegador, sem a necessidade de ferramentas extras.

## Certifique-se de que a estrutura do diretório translations esteja configurada conforme o Flask-Babel exige, com arquivos .po e .mo devidamente compilados.

Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## Estrutura do Projeto
```bash

.
├── app.py
├── requirements.txt
├── templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── admin.html
│   ├── user.html    # Página que lista usuários e possui paginação
│   └── navbar.html
├── static
│   └── images       # Contém ícones de bandeiras (opcional)
└── translations
    ├── en
    │   └── LC_MESSAGES
    │       ├── messages.po
    │       └── messages.mo
    ├── es
    │   └── LC_MESSAGES
    │       ├── messages.po
    │       └── messages.mo
    └── pt_BR
        └── LC_MESSAGES
            ├── messages.po
            └── messages.mo


