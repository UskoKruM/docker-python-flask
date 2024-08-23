FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

#ENV SECRET_KEY=******

CMD ["flask", "run", "--host=0.0.0.0"]