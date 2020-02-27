FROM rasa/rasa

ADD ./app /app
WORKDIR /app

RUN rasa train

ENTRYPOINT ["bash", "/app/scripts/start_services.sh"]