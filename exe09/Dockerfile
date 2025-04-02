FROM python:3.11-slim

WORKDIR /exe09

RUN pip install streamlit pandas plotly

COPY . .

EXPOSE 8509

CMD ["streamlit", "run", "exe09.py", "--server.port=8509", "--server.address=0.0.0.0"] 