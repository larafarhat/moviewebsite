# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY . /app/

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the application
# NOTE: In a production environment, you would use a production-ready web server like Gunicorn or uWSGI
# For this example, the Django development server is sufficient.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]