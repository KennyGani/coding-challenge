# 
FROM python:3.9

# 
WORKDIR /school

# 
COPY ./requirements.txt /requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

# 
COPY ./ /school/

# 
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "80"]

