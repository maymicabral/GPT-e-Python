# GPT e Python: Criando Ferramentas com API

Este repositório apresenta os conhecimentos e práticas desenvolvidos durante o curso **GPT e Python: Criando Ferramentas com API**, realizado pela Alura. O curso abrange conceitos e técnicas essenciais para utilização da API do ChatGPT, integração com aplicações e implementações práticas em Python.

## Conteúdo do Curso

### 1. Interações com a API do ChatGPT
- Aprendizado sobre como realizar requisições e obter respostas do ChatGPT via API.
- Configuração de fontes de chaves de API de forma segura.

### 2. Configuração de Parâmetros
- Entendimento e configuração dos parâmetros da API, como temperatura, top_p, entre outros.

### 3. Conceitos de Assistentes e Threads
- Exploração do Playground da OpenAI para criação e gerenciamento de assistentes e threads.

### 4. Modelos e Custos
- Diferenças entre os modelos da OpenAI (GPT-3.5, GPT-4, etc.).
- Cálculo de custos baseado no número de tokens e seleção do modelo adequado para cada caso.

### 5. Prompt Engineering e Prompt Template
- Introdução aos conceitos de prompt engineering e a criação de prompt templates.
- Boas práticas para otimização de respostas do ChatGPT.

### 6. Processamento em Lote e Controle de Erros
- Execução de requisições em lote.
- Tratamento de erros e boas práticas para garantir resiliência na aplicação.

### 7. Prática: Análise de Fraudes
- Implementação prática de análise de fraudes utilizando o ChatGPT e Python.

## Estrutura do Repositório

- `src/`: Códigos fonte das práticas realizadas no curso.
- `notebooks/`: Notebooks com exemplos e experimentos realizados.
- `docs/`: Documentação adicional sobre a API e modelos.

## Duração do Curso

- **Playground e a API da OpenAI**: 38 minutos (14 aulas).
- **Prompt Engineering e Prompt Template**: 20 minutos (7 aulas).
- **Custos, Modelos e Contagem de Tokens**: 18 minutos (8 aulas).
- **Batch e Controle de Erros**: 19 minutos (10 aulas).
- **Praticando: Análise de Fraudes**: Projetos práticos.

## Requisitos

- Python 3.7+
- Biblioteca `openai`
- Conhecimentos básicos de manipulação de APIs

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure sua chave de API da OpenAI no arquivo `.env`:
   ```env
   OPENAI_API_KEY=sua-chave-aqui
   ```
4. Execute os exemplos:
   ```bash
   python src/exemplo.py
   ```

## Considerações Finais

Este curso proporciona uma base sólida para profissionais interessados em integrar soluções de IA em seus projetos. Ele abrange desde os fundamentos até a aplicações práticas, preparando você para criar ferramentas inteligentes e eficientes com Python e a API do ChatGPT.