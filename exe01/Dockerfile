FROM python:3.11-slim

WORKDIR /exe01

RUN pip install streamlit pandas numpy plotly.express

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "exe01.py", "--server.port=8501", "--server.address=0.0.0.0"]