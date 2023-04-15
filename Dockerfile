FROM python:latest

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install requests flask
COPY . /app

WORKDIR /app

CMD ["python", "app.py"]

EXPOSE 5000