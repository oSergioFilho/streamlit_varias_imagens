FROM python:3.11-slim

WORKDIR /exe05

RUN pip install streamlit 

COPY . .

EXPOSE 8505

CMD ["streamlit", "run", "exe05.py", "--server.port=8505", "--server.address=0.0.0.0"] 