# Description: Dockerfile for the backend Django application
FROM python:3.10-slim


# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*


#  Set working directory
WORKDIR /usr/src/app


# Install dependencies
COPY Tekisite/requirements/base.txt ./

RUN pip install --no-cache-dir -r base.txt


# Copy project files
COPY . .

# CMD [ "pwd" ]
# Expose the port the app runs in
EXPOSE 8000


# Serve the app
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
CMD ["sh", "-c", "cd Tekisite &&pwd && ls && python manage.py runserver 0.0.0.0:8000"]

