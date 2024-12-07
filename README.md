# Lumin

Lumin é uma plataforma de geração e análise de linguagem natural que utiliza LangGraph, LLaMA 3 e Redis como tecnologias fundamentais. O objetivo do Lumin é fornecer uma ferramenta completa para a criação de textos personalizados, análise de linguagem natural e gerenciamento de semântica.

**Projeto:** Lumin - Chatbot Inteligente com Aprendizado em Tempo Real

**Objetivo:** Desenvolver um chatbot interativo que aprende e se adapta com base nas interações do usuário, armazenando informações relevantes sobre um tema específico.

**Características do chatbot:**
* Responde perguntas com base nas interações do usuário
* Aprende e se adapta com base nas interações do usuário
* Armazena informações relevantes sobre um tema específico apenas quando o usuário enviar algo verdadeiro ou quando se trata de preferências

**Melhorias adicionais:**

* Aceita correções falsas é limitada, garantindo que as informações armazenadas sejam precisas.
* Fornece opção para escolher um tom mais formal ou informal.

## Tecnologias utilizadas:
* LangGraph: análise de linguagem natural
* LLaMA 3: modelo de linguagem natural baseado em Transformers
* Redis: banco de dados NoSql completo (utilizado como base de dados vetorial)
* Streamlit: framework para desenvolvimento de interfaces gráficas

## Como usar
1. Baixe o repositório do Lumin e instale as dependências necessárias.
2. Rode a aplicação com `docker-compose up`.
3. Acesse a interface gráfica em `http://localhost:8501`.


# Licença
O Lumin é distribuído sob a licença MIT. Para mais informações, consulte o arquivo LICENSE.md.
