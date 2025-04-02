FROM python:3.11-slim

WORKDIR /exe06

RUN pip install streamlit wordcloud matplotlib

COPY . .

EXPOSE 8506

CMD ["streamlit", "run", "exe06.py", "--server.port=8506", "--server.address=0.0.0.0"] 