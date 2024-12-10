# ChatBot Lumin
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/andresinho20049/chatbot-lumin/blob/main/README.pt-br.md)

A dynamic web-based chatbot powered by Ollama and LangChain, utilizing Streamlit as the frontend framework. This project aims to provide an interactive conversational experience with advanced prompt templates that consider user context, preferences, and query.

## Features
* Web-based interface built using Streamlit
* Integration with Ollama model for natural language processing
* Advanced prompt templates to handle user context, preferences, and query
* Dynamic home page with curiosity-driven content
* Model configuration through page settings (model name and URL)
* Redis vector database for storing user data

## :movie_camera: Preview
![Preview](https://github.com/andresinho20049/chatbot-lumin/blob/main/public/preview.gif)

## Technology Stack
* **Streamlit**: Frontend framework for building web applications
* **LangChain**: Library for natural language processing and conversation management
* **Ollama**: Model for conversational AI
* **Redis**: Vector database for storing user data
* **Docker**: Containerization platform for running the project

### Docker Compose
This project uses two separate Docker Compose files:

* `docker-compose.dev.yml`: For development mode, reflecting code updates in real-time
* `docker-compose.yml`: For production mode, but I do not recommend it as ideal for use in production, it is better to use other orchestrators such as Kubernetes or AWS ECS.

### Ollama Entrypoint (ollama-entrypoint.sh)
The `ollama-entrypoint.sh` script is used to pull the model when the container starts.

## Get Started
1. Clone the repository using 
    ```sh
    git clone https://github.com/andresinho20049/chatbot-lumin.git
    ```
2. Run the containers using 
    * `docker compose up` \
    Ou 
    * `docker compose -f ./docker-compose.dev.yml up` to _dev mode_
3. Open the web interface in your browser at `http://localhost:8501`

### Requirements
* Docker
* Docker Compose

## Important Considerations
* **First Run Time**: The first run of the project may take a significant amount of time, potentially several minutes, due to the following reasons:
	+ Docker will pull the required images from the registry, which can be a slow process.
	+ Ollama will download and load the model used in the project, which can also take some time.
* **Image Download**: If you don't have the required images installed on your system, docker will need to pull them from the registry. This can add significant time to the first run.
* **Model Loading**: Similarly, if Ollama needs to download and load the model used in the project, this can also take some time.
* **System Resources**: The first run may also require a significant amount of system resources, including CPU, memory, and disk space. This is because docker will need to create containers, pull images, and Ollama will need to load the model.

* **Tips for Faster First Run**
    * **Use a Local Registry**: If you have access to a local Docker registry, you can use it instead of pulling images from the public registry. This can significantly speed up the first run.
    * **Pre-Download Images**: You can pre-download the required images using `docker pull` command before running the project.
    * **Use a Faster Internet Connection**: If you have a fast internet connection, this can also help reduce the time taken for docker to pull the images and Ollama to load the model.
    * **Increase System Resources**: Ensure that your system has sufficient resources (CPU, memory, disk space) to handle the first run.

By considering these factors, you can plan accordingly and take steps to optimize the first run of the project.

**Ollama Server running on GPU**
> **Note**: Docker Compose was configured to run the model with optimal performance, adding attributes to use the GPU considering NVIDIA's RTX GPU. If your PC doesn't have a GPU with this configuration, simply comment out the attributes as shown below.

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
[Learn how to run Ollama with Docker on the GPU](https://github.com/ollama/ollama/blob/main/docs/docker.md)

**Available Memory**

* There is a possible issue when running Ollama serve with Docker Compose, where the model may not receive enough memory for execution. \
This problem does not occur when running the container with `docker run`.
* If you encounter this issue, please try running the model using one of the following scripts, specifying the correct network:
```sh
sudo docker run -d --privileged --runtime=nvidia --gpus all -p 11434:11434 --network chat_lumin_lumin-network -v ./data/ollama:/root/.ollama --name ollama --restart always ollama/ollama
```

or the following command if you cannot run it on a GPU:

```sh
sudo docker run -d -p 11434:11434 --network chat_lumin_lumin-network -v ./data/ollama:/root/.ollama --name ollama --restart always ollama/ollama
```

**Future Improvements**

While the current implementation provides a solid foundation for conversational AI, there's room for improvement:

* **Training with PyTorch**: Install transform dependencies to tokenize the model and create new models based on the embedded Ollama model. This will enable training the model using libraries like PyTorch.
* **Integration with other NLP models**: Explore integrating additional NLP models to enhance conversational capabilities.
* **Implement a class model** to persist structured data on Redis
* **Add support for more data types** (e.g. integers, floats, lists, dictionaries)
* **Implement transactions** using Redis transactions (multi/exec methods)
* **Improve memory efficiency**: Optimize the use of memory to reduce system pressure and improve performance.
* **Add support for additional languages**: Allow the model to converse in different languages, including non-Latinized languages.
* **Implement advanced AI functionalities**: Explore integrating more advanced AI models, such as recurrent neural networks and deep learning.

These improvements can help significantly enhance the model's performance and ability to handle complex conversations.

## :copyright: Copyright
**Developed by** [Andresinho20049](https://andresinho20049.com.br/) | [https://andresinho20049.com.br/](https://andresinho20049.com.br/) \
**Project**: ChatBot Lumin
Utilizing **Streamlit** to build a web application, combined with the conversational AI capabilities of **Langchain**, and deployed using **Docker** containers. The platform leverages **Redis** as a vector database to store and manage large amounts of semantic data, enabling fast and efficient querying and retrieval of information.

This implementation allows for intelligent and personalized interactions with users, leveraging cutting-edge technologies to create a unique conversational experience. As users interact with the chatbot, it can learn and improve over time, allowing it to acquire new knowledge and skills based on feedback and analysis.

**Considerations**
* Built using **Python**, this platform is designed to be flexible and adaptable to changes in technologies and natural language, ensuring that it continues to meet the needs of users.
* Deployed using **Docker**, which enables fast and efficient deployment of the application.
* The use of **Redis** as a vector database provides a scalable and performant solution for storing and managing large amounts of semantic data.
* This platform is designed to learn and improve over time, allowing it to adapt to changing user needs and preferences.