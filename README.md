# Envio de Mensagens WhatsApp - Supabase + Z-API

Este projeto envia mensagens personalizadas para contatos armazenados no Supabase utilizando a Z-API.  
Mensagem enviada: **"Olá {{nome_contato}}, tudo bem com você?"**

- O script busca contatos via função `get_contacts(limit=3)` do repositório.  
- O parâmetro `limit` define a **quantidade máxima de contatos** a serem retornados do banco (ex.: 3 contatos por execução).

---

## 🔧 Pré-requisitos

- Python 3.9+
- Conta Supabase (com tabela `contacts`)
- Conta Z-API (instância configurada)

---

## 🗂 Estrutura do projeto

```
project/
│
├─ main.py # Script principal para enviar mensagens
├─ .env # Variáveis de ambiente
├─ services/
│    └─ zapi_service.py # Serviço de envio via Z-API
└─ repositories/
└─ contacts_repository.py # Conexão com Supabase
```
## ⚙️ Setup

1. Clone o projeto:

```bash
git clone https://github.com/whoisjose569/desafio-b2bflow
```
Instale as dependências:
pip install -r requirements.txt

Configure o .env com suas credenciais:
## Supabase
```
SUPABASE_URL=https://SEU_PROJETO.supabase.co
SUPABASE_KEY=SEU_ANON_KEY
````
## Z-API
```
ZAPI_INSTANCE_ID=SEU_INSTANCE_ID
ZAPI_TOKEN=SEU_INSTANCE_TOKEN
ZAPI_CLIENT_TOKEN=SEU_CLIENT_TOKEN
```
## Crie a tabela contacts no Supabase:

```
create table contacts (
    id bigint generated always as identity primary key,
    name text not null,
    number text not null
);
```
## Como rodar

```
python main.py
```

## 📝 Boas práticas aplicadas

.env para variáveis sensíveis

Funções separadas em services e repositories

Tratamento básico de erros

Limite de contatos configurável via get_contacts(limit=3)

## 📌 Observações

Garanta que a instância Z-API esteja conectada (ícone verde no painel).
