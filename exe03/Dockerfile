FROM python:3.11-slim

WORKDIR /exe03

RUN pip install streamlit pandas numpy plotly.express

COPY . .

EXPOSE 8503

CMD ["streamlit", "run", "exe03.py", "--server.port=8503", "--server.address=0.0.0.0"]