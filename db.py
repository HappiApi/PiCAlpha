import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse("postgres://vdbennzvevmumz:4IyA_mZ8eHxsKN1go1yrpUa_FI@ec2-54-204-20-209.compute-1.amazonaws.com:5432/d9js65ocv8ilj7")

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)
