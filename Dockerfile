FROM python:3.10
ENV DEBUG=True
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x wait-for-it.sh
