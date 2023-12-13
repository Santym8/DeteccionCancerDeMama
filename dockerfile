FROM python:3.7

RUN pip install --upgrade pip

RUN pip install django
RUN pip install keras
RUN pip install numpy
RUN pip install tensorflow
RUN pip install joblib
RUN pip install scikit-learn

COPY . code
WORKDIR /code

EXPOSE 8000

ENTRYPOINT ["python", "./manage.py"]
CMD ["runserver", "0.0.0.0:8000"]