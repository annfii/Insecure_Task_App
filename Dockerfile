FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

ENV FLASK_APP app
ENV FLASK_ENV development

EXPOSE 5001

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
