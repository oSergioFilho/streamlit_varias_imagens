FROM python:3.11-slim

WORKDIR /exe07

RUN pip install streamlit pandas plotly

COPY . .

EXPOSE 8507

CMD ["streamlit", "run", "exe07.py", "--server.port=8507", "--server.address=0.0.0.0"] 