FROM python:3.7-slim
WORKDIR /app
COPY . .
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
RUN python manage.py collectstatic --no-input
LABEL author='Shamaiski Ivan' version=1 email='shamaiskii.ivan@gmail.com'
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]
