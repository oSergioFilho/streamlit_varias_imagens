FROM python:3.11-slim

WORKDIR /exe04

RUN pip install --no-cache-dir streamlit pandas numpy

COPY . .

EXPOSE 8504

CMD ["streamlit", "run", "exe04.py", "--server.port=8504", "--server.address=0.0.0.0"] 