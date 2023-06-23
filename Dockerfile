FROM python:3.8

WORKDIR /src
ENV PYTHONPATH=/src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src /src

EXPOSE 8000

CMD ["uvicorn", "app.entrypoints.fastapi_app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

