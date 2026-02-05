# Pipeline de Engenharia de Dados - Salários

Este projeto constrói um pipeline ETL para analisar salários de engenharia de dados usando Docker e Python.

## Arquitetura

1. **Infraestrutura:** Docker Compose com PostgreSQL 16 (Alpine).
2. **Ingestão:** Script Python que lê e carrega no banco.
3. **Armazenamento:** PostgreSQL.

## Como rodar

1. Clone o repositório.
2. Crie o arquivo de senha:
   ```bash
   mkdir db
   echo "sua_senha" > db/password.txt
   ```

3. Crie seu ambiente virtual e instale as dependências:

   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

   ```bash
   # Linux / Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

   ```bash
   # Instalar bibliotecas
   pip install -r requirements.txt 
   ```

4. Suba o banco de dados e rode o pipeline:
   # Sobe o banco Postgres
   ```bash
   docker compose up -d
   python etl_pipeline.py
   ```
