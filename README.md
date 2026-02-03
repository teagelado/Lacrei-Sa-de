# 🏥 Lacrei Saúde - API de Gerenciamento

Esta é uma API desenvolvida para o voluntariado da **Lacrei Saúde**. O sistema permite o gerenciamento de profissionais de saúde e o agendamento de consultas, focando em acessibilidade e organização.

## 🚀 Tecnologias Utilizadas
* **Python 3.12**
* **Django 5.x**
* **Django REST Framework (DRF)**: Para a criação da API.
* **SQLite**: Banco de dados padrão para desenvolvimento.
* **GitHub Actions**: Automação de testes (CI/CD).

## ⚙️ Funcionalidades
- [x] Cadastro e listagem de profissionais.
- [x] Agendamento de consultas vinculado a profissionais.
- [x] Validação de dados (ex: nome do profissional com mínimo de 3 caracteres).
- [ ] Integração com API Asaas para Split de Pagamentos (Próxima Fase).

## 🛠️ Como rodar o projeto localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/teagelado/Lacrei-Sa-de.git](https://github.com/teagelado/Lacrei-Sa-de.git)
Crie e ative o ambiente virtual:

Bash
python -m venv venv
.\venv\Scripts\activate
Instale as dependências:

Bash
pip install django djangorestframework django-cors-headers
Rode as migrações e inicie o servidor:

Bash
python gerenciar.py migrate
python gerenciar.py runserver
Acesse: http://127.0.0.1:8000/api/profissionais/

🧪 Testes
Para garantir a qualidade do código, rode:

Bash
python gerenciar.py test
