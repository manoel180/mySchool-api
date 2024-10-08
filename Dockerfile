# 
FROM python:3.10

# 
WORKDIR /app

# 
COPY ./requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# 
COPY . /app



#


ENTRYPOINT ["./create_superuser_prod.sh"]
EXPOSE 8080