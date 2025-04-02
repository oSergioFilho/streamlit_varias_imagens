FROM python:3.11-slim

WORKDIR /exe02

RUN pip install streamlit pandas numpy

COPY . .

EXPOSE 8502

CMD ["streamlit", "run", "exe02.py", "--server.port=8502", "--server.address=0.0.0.0"]
