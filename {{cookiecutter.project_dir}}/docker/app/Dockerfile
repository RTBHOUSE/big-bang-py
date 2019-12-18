FROM python:{{ cookiecutter.python_version }}

ARG UID
ARG GID
RUN groupadd -g ${GID} appuser \
    && useradd -m -u ${UID} -g appuser appuser

WORKDIR /app

COPY --chown=appuser:appuser requirements/requirements.txt requirements/requirements.txt
RUN pip install -r requirements/requirements.txt

COPY --chown=appuser:appuser . /app

USER appuser
