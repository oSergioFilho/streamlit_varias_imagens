FROM python:3.11-slim

WORKDIR /exe10

COPY . .

# Instala dependências do sistema (certificados SSL)
RUN apt-get update && apt-get install -y ca-certificates && \
    pip install streamlit requests pandas plotly && \
    apt-get clean

EXPOSE 8510

CMD ["streamlit", "run", "exe10.py", "--server.port=8510", "--server.address=0.0.0.0"]
