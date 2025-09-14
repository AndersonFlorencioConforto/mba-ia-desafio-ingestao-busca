# Desafio MBA Engenharia de Software com IA - Full Cycle

Este repositório contém uma solução de ingestão e busca baseada em vetores usando OpenAI e PGVector.

## Estrutura relevante
- `src/ingest.py` — script de ingestão (carrega dados e popula a coleção vetorial).
- `src/search.py` — lógica de busca por similaridade e template de prompt.
- `src/chat.py` — interface CLI para perguntar ao sistema (suporta modo único e modo interativo em loop).

## Variáveis de ambiente necessárias
Crie um arquivo `.env` com as seguintes variáveis (ou exporte no ambiente):

- `OPENAI_API_KEY` — sua chave OpenAI.
- `OPENAI_EMBEDDING_MODEL` — (opcional) modelo de embedding (ex: `text-embedding-3-small`).
- `DATABASE_URL` — URL de conexão com o Postgres que contém a extensão PGVector.
- `PG_VECTOR_COLLECTION_NAME` — nome da coleção/índice no PGVector.

Existe um arquivo exemplo `.env.example` com o formato esperado.

## Instalação
Recomenda-se criar um ambiente virtual e instalar dependências:

PowerShell:
```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
```

## Uso — CLI (`src/chat.py`)
O `chat.py` é um CLI simples que envia uma pergunta para o pipeline de busca e imprime a resposta.

- Pergunta única (argumento):
```powershell
python .\src\chat.py "Qual é a capital da França?"
```

- Usando pipe / stdin:
```powershell
echo "Qual é a capital da França?" | python .\src\chat.py
```


Observações:
- Se o script encontrar um objeto de resposta com atributo `content`, ele imprimirá esse conteúdo; caso contrário, imprimirá o retorno bruto.
- Se variáveis de ambiente obrigatórias estiverem faltando, o script levantará um erro na inicialização — verifique `.env`.

## Ingestão
Use `src/ingest.py` para carregar documentos e popular a coleção vetorial (veja comentários no script para parâmetros e uso).

## Docker
O repositório inclui um `docker-compose.yml` que pode ser usado para subir um Postgres com PGVector e serviços relacionados. Ajuste as variáveis de ambiente conforme necessário antes de executar.

## Testes e execução
- Verifique se seu banco Postgres e a coleção PGVector estão acessíveis pelo `DATABASE_URL`.
- Execute `python .\src\chat.py` e faça perguntas para validar o comportamento.

