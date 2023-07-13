# from https://towardsdatascience.com/how-to-deploy-a-machine-learning-model-with-fastapi-docker-and-github-actions-13374cbd638a
FROM python:3.10-slim

# # from https://stackoverflow.com/a/55032822/14403987
# # needed for python:3.10.12-alpine3.18
# RUN apk --no-cache add musl-dev linux-headers g++
RUN pip install fastapi uvicorn pandas scikit-learn

COPY main.py /app/main.py
COPY src/models/* /app/src/models/

ENV PYTHONPATH=/app
WORKDIR /app

EXPOSE 8000

ENTRYPOINT [ "uvicorn" ]
CMD [ "main:app", "--host", "0.0.0.0",  "--proxy-headers", "--forwarded-allow-ips '*' "]

# RUN pip install fastapi uvicorn spacy

# COPY ./api /api/api

# ENV PYTHONPATH=/api
# WORKDIR /api

# EXPOSE 8000

# ENTRYPOINT ["uvicorn"]
# CMD ["api.main:app", "--host", "0.0.0.0"]