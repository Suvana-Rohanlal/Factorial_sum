FROM python:3

# set a directory for the app
WORKDIR .

# copy all the files to the container
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
COPY . .

# run the command
CMD ["python", "./app.py"]
