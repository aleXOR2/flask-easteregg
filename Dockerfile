FROM python:3.6

LABEL maintainer "Alex So <alex.so@something.com>"

ARG A_VERSION
ENV VERSION=${A_VERSION}

COPY ./src/* /app/

WORKDIR /app

RUN useradd -r app \
    && chown -R app /app

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python \
    && . $HOME/.poetry/env \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev


EXPOSE 5000

USER app

ENTRYPOINT [ "python", "./easter_egg.py" ]

# CMD ["./easter_egg.py"]