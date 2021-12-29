FROM python:3.7

WORKDIR /code

COPY . .

RUN pip freeze > requirements.txt

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
