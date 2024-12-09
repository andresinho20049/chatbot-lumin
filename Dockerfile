# Base Stage
FROM python:3.9-slim AS base
WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# ---
# Dev Stage
FROM base AS dev
ENV STREAMLIT_MODE=dev

VOLUME public /app/public
VOLUME src /app/

# ENTRYPOINT ["streamlit", "run", "app.py"]
# ---


# Run Stage
FROM base AS run
ENV STREAMLIT_MODE=prod

COPY ./public /app/public
COPY ./src /app/

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--ui.hideTopBar=true"]