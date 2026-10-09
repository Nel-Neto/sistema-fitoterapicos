# Sistema de Fitoterápicos

Aplicação web em Python/Flask conectada ao banco MySQL `fitoterapicos`.

## 1. Pré-requisitos

- Python 3.11 ou superior
- MySQL 8.x
- Banco `fitoterapicos` já importado
- VS Code

## 2. Abrir o projeto

Abra a pasta `sistema_fitoterapicos` no VS Code.

## 3. Criar o ambiente virtual

No terminal do VS Code:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
.venv\Scripts\activate
```

## 4. Instalar dependências

```bash
pip install -r requirements.txt
```

## 5. Configurar o MySQL

Copie `.env.example` para um novo arquivo chamado `.env`.

Exemplo:

```env
DB_USER=root
DB_PASSWORD=SUA_SENHA
DB_HOST=localhost
DB_PORT=3306
DB_NAME=fitoterapicos
SECRET_KEY=uma-chave-local
```

Não envie o arquivo `.env` para repositórios públicos.

## 6. Executar

```bash
python app.py
```

Abra no navegador:

`http://127.0.0.1:5000`

## Funcionalidades

- Página inicial
- Listagem alfabética dos fitoterápicos
- Busca por nome popular
- Busca por nome científico
- Busca por família botânica
- Busca por indicação terapêutica
- Página detalhada com dados relacionados do banco
- Páginas de erro 404 e 500
- Layout responsivo com Bootstrap

## Estrutura

```text
sistema_fitoterapicos/
├── app.py
├── config.py
├── requirements.txt
├── .env.example
├── models/
├── routes/
├── templates/
└── static/
```

## Próximas evoluções sugeridas

- painel administrativo;
- autenticação;
- cadastro e edição de fitoterápicos;
- filtros avançados;
- referências bibliográficas;
- API JSON;
- imagens das plantas;
- testes automatizados.
