# Pipeline de Engenharia de Dados - Salários

Este projeto constrói um pipeline ETL automatizado para analisar salários de engenharia de dados usando Docker e Python.

## 🏗️ Arquitetura

1. **Infraestrutura:** Docker Compose com PostgreSQL 16 (Alpine).
2. **Ingestão:** Script Python que baixa dados do Kaggle e carrega no banco.
3. **Armazenamento:** PostgreSQL com modelagem de dados tipada e persistência via volumes.

## 🚀 Como rodar

1. Clone o repositório.
2. Crie o arquivo de senha:
   ```bash
   mkdir db
   echo "sua_senha_secreta" > db/password.txt