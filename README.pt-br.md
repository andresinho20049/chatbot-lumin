# ChatBot Lumin 
[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/andresinho20049/chatbot-lumin/blob/main/README.md)

Um chatbot dinâmico baseado na web, desenvolvido com Streamlit e Ollama, utilizando LangChain para gestão de conversas avançadas. Este projeto tem como objetivo fornecer uma experiência de conversação interativa com templates de prompts avançados que consideram o contexto do usuário, suas preferências e a consulta.

## Características
* Interface web construída com Streamlit
* Integração com Ollama para processamento de linguagem natural
* Templates de prompts avançados para lidar com o contexto do usuário, preferências e consulta
* Página inicial dinâmica com conteúdo curioso
* Configuração do modelo através da página de configurações (nome do modelo e URL)
* Armazenamento de dados do usuário usando Redis como banco de vetores

## :movie_camera: Preview
![Preview](https://github.com/andresinho20049/chatbot-lumin/blob/main/public/preview.gif)

## Tecnologias Utilizadas
* **Streamlit**: Framework para desenvolvimento de aplicativos web
* **LangChain**: Biblioteca para processamento de linguagem natural e gestão de conversas
* **Ollama**: Modelo para IA conversacional
* **Redis**: Banco de vetores para armazenar dados do usuário
* **Docker**: Plataforma de containerização para executar o projeto

### Docker Compose
Este projeto utiliza dois arquivos `docker-compose` separados:

* `docker-compose.dev.yml`: Para modo desenvolvimento, refletindo atualizações em tempo real no código
* `docker-compose.yml`: Para modo produtivo, mas não recomendo como ideal para utilizar em produção, melhor utilizar outros orquestradores como Kubernetes ou ECS da AWS.

### Ollama Entrypoint (ollama-entrypoint.sh)
O script `ollama-entrypoint.sh` é utilizado para baixar o modelo quando o container iniciar.

## Obtenha começado
1. Faça o download do projeto utilizando 
    ```sh
    git clone`: `https://github.com/andresinho20049/chatbot-lumin.git
    ```
2. Execute os containers utilizando: 
    * `docker compose up` \
    Ou 
    * `docker compose -f ./docker-compose.dev.yml up` para _dev mode_
3. Abra a interface web no seu navegador em `http://localhost:8501`

### Requisitos
* Docker
* Docker Compose

### Considerações Importantes
* **Tempo da Execução Inicial**: A execução inicial do projeto pode levar um tempo significativo, especialmente se você não tiver as images necessárias instaladas no seu sistema, pois o Docker precisará baixar as images e o Ollama precisará carregar o modelo utilizado.
* **Download das Images**: Se você não tiver as images necessárias instaladas no seu sistema, o Docker precisará baixá-las do registro. Isso pode levar um tempo significativo.
* **Carregamento do Modelo**: Da mesma forma, se o Ollama precisar baixar e carregar o modelo utilizado, isso também pode levar algum tempo.
* **Recursos do Sistema**: A execução inicial pode requerer uma quantidade significativa de recursos do sistema, incluindo processador, memória e espaço em disco. Isso ocorre porque o Docker precisa criar contêineres, baixar images e o Ollama precisa carregar o modelo.

* **Dicas para Execução Inicial mais Rápida**

    * **Use um Registro Local**: Se você tiver acesso a um registro local do Docker, pode usar ele em vez de baixar as images do registro público. Isso pode acelerar significativamente a execução inicial.
    * **Pre-Baixa Images**: Você pode pre-baixar as images necessárias usando o comando `docker pull` antes de executar o projeto.
    * **Use uma Conexão com Internet Rápida**: Se você tiver uma conexão com internet rápida, isso também pode ajudar a reduzir o tempo necessário para o Docker baixar as images e o Ollama carregar o modelo.
    * **Aumente os Recursos do Sistema**: Certifique-se de que seu sistema tenha recursos suficientes (processador, memória, espaço em disco) para lidar com a execução inicial.

Essas considerações podem ajudá-lo a planejar e tomar medidas para otimizar a execução inicial do projeto.

**Ollama Server rodando pela GPU**
> **Observação importante**: o Docker Compose foi configurado para rodar o modelo com o melhor desempenho, adicionando atributos para usar a GPU considerando uma NVIDIA RTX. \
Se seu PC não tiver uma GPU com essas configurações, basta comentar os atributos como exemplificado abaixo.

```docker
  ollama:
    image: ollama/ollama
    ports:
        - 11434:11434
    volumes:
      - ./data/ollama:/root/.ollama
      - ./ollama-entrypoint.sh:/entrypoint.sh
    container_name: ollama
    pull_policy: always
    tty: true
    restart: always
    entrypoint: ["/usr/bin/bash", "/entrypoint.sh"]
    # environment:
    #   - gpus=all
    # deploy:
    #   resources:
    #     reservations:
    #       memory: 4096m
    #       devices:
    #       - driver: nvidia
    #         capabilities: ["gpu"]
    #         count: all
    networks:
      - lumin-network
```

[Saiba como rodar Ollama com Docker pela GPU](https://github.com/ollama/ollama/blob/main/docs/docker.md)

**Memoria Disponivel**

* É possível que você encontre problemas ao executar o contêiner Ollama com Docker Compose, pois o modelo pode não receber a memória necessária para execução. \
Isso não ocorre quando o container é executado utilizando `docker run`.
* Se você encontrar esse problema, tente executar o modelo utilizando o script abaixo, especificando corretamente a rede:
```sh
sudo docker run -d --privileged --runtime=nvidia --gpus all -p 11434:11434 --network chat_lumin_lumin-network -v ./data/ollama:/root/.ollama --name ollama --restart always ollama/ollama
```
ou utilize o comando abaixo se não for possível executar usando a GPU:
```
sudo docker run -d -p 11434:11434 --network chat_lumin_lumin-network -v ./data/ollama:/root/.ollama --name ollama --restart always ollama/ollama
```

**Melhorias Futuras**

Embora a implementação atual forneça uma base sólida para IA conversacional, há espaço para melhorias:

* **Treinamento com PyTorch**: Instale dependências de transformação para tokenizar o modelo e criar novos modelos com base no modelo Ollama embutido. Isso permitirá a treinamento do modelo utilizando bibliotecas como PyTorch.
* **Integração com outros modelos NLP**: Explorar a integração de modelos NLP adicionais para melhorar as capacidades conversacionais.
* **Implementar um modelo classe** para persistir dados estruturados no Redis
* **Adicionar suporte a mais tipos de dados** (por exemplo, integers, floats, lists, dictionaries)
* **Implantar transações** utilizando transações do Redis (multi/exec métodos)
* **Melhorar a eficiência da memória**: otimizar o uso de memória para reduzir a pressão no sistema e melhorar o desempenho.
* **Adicionar suporte a linguagens adicionais**: permitir que o modelo converse em diferentes idiomas, incluindo idiomas não latinizados.
* **Implementar funcionalidades de IA avançadas**: explorar a integração de modelos de IA mais avançados, como redes neurais recorrentes e aprendizado profundo.

Essas melhorias podem ajudar a melhorar significativamente o desempenho do modelo e sua capacidade de lidar com conversações complexas.

## :copyright: Copyright
**Desenvolvido por** [Andresinho20049](https://andresinho20049.com.br/) | [https://andresinho20049.com.br/](https://andresinho20049.com.br/) \
**Projeto**: ChatBot Lumin
Utilizando **Streamlit** para construir uma aplicação web, combinada com as capacidades de IA conversacional do **Langchain**, e implantado em contêineres **Docker**. A plataforma utiliza o **Redis** como banco de vetores (vector database) para armazenar e gerenciar grandes quantidades de dados semânticos, permitindo consultas e recuperação de informações com eficiência.

Essa implementação permite interações inteligentes e personalizadas com os usuários, utilizando tecnologias de ponta para criar uma experiência conversacional única. À medida que os usuários interagem com o chatbot, ele pode aprender e melhorar ao longo do tempo, permitindo que ele adquira novas habilidades e conhecimentos com base em feedback e análise.

**Considerações**
* Desenvolvido utilizando **Python**, essa plataforma é projetada para ser flexível e adaptável às mudanças nas tecnologias e na linguagem natural, garantindo que ela continue a atender às necessidades dos usuários.
* Implantado utilizando **Docker**, o que permite uma implementação rápida e eficiente da aplicação.
* O uso do **Redis** como banco de vetores fornece uma solução escalável e performante para armazenar e gerenciar grandes quantidades de dados semânticos.
* Essa plataforma é projetada para aprender e melhorar ao longo do tempo, permitindo que ela se adapte às necessidades e preferências dos usuários em constante mudança.