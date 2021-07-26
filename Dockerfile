FROM python:3

# set a directory for the app
WORKDIR .

# copy all the files to the container
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy all the files to the container
COPY src/ .

# set entry point
ENTRYPOINT ["python", "./factorial_sum.py"]
