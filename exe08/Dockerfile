FROM python:3.11-slim

WORKDIR /exe08

RUN pip install streamlit numpy pandas scikit-learn plotly

COPY . .

EXPOSE 8508

CMD ["streamlit", "run", "exe08.py", "--server.port=8508", "--server.address=0.0.0.0"] 