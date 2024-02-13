# 
FROM python:3.11

# 
COPY /backend/compose/requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./backend/ /code/app

# 
WORKDIR /code

# 
#CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000"]
CMD [ "python",  "/code/app/main.py"]