Visualize a aplicação real através do link no final deste README.md.

---

## 🔹 Estrutura do projeto

```
project/
├─ app/
│   ├─ __init__.py            # create_app()
│   ├─ config.py              # Config / env
│   ├─ extensions.py          # DB (psycopg, etc)
│   │
│   ├─ routes/
│   │   ├─ __init__.py        # registra blueprints
│   │   ├─ pages.py           # rotas HTML
│   │   └─ api.py             # rotas REST (JSON)
│   │
│   ├─ services/              # regras de negócio
│   │   └─ __init__.py        # pacote services (NÃO blueprint)
│   │
│   ├─ repositories/          # acesso ao banco (SQL)
│   │   └─ __init__.py        # pacote repositories
│   │
│   ├─ templates/             # Jinja2
│   │   ├─ base.html
│   │   ├─ home.html
│   │   ├─ menu.html
│   │   └─ produtos.html
│   │
│   └─ static/                # arquivos estáticos
│       ├─ css/
│       │   └─ style.css
│       ├─ js/
│       │   └─ main.js
│       ├─ images/
│       │   ├─ banners/
│       │   ├─ logos/
│       │   └─ users/
│       └─ fonts/
│           └─ inter.woff2
│
├─ migrations/                # Alembic / Flask-Migrate
├─ tests/                     # pytest
├─ run.py                     # entrypoint da aplicação
├─ requirements.txt
├─ Procfile                   # Cloud - Railway
├─ README.md                  # Documentação principal
├─ .env                       # NÃO versionar
├─ .gitignore
└─ pyproject.toml             # opcional
```
---

## ⚙️ Tecnologias Utilizadas
* Python (Flask)
* HTML5
* CSS3
* JavaScript (Vanilla)
* Jinja2
* LocalStorage

---

## ▶️ Como Rodar o Projeto

```
pip install -r requirements.txt
python run.py

Depois, acesse no navegador:

http://127.0.0.1:5000
```
---

## 📌 Observações
* O sistema não utiliza login
* Os dados da compra atual ficam salvos localmente no navegador
* O cadastro de produtos é persistido no banco de dados
* Projeto ideal para uso pessoal ou familiar

---

## 👨‍💻 Autor 
Desenvolvido por Eduardo Libório
📧 eduardosoleno@protonmail.com