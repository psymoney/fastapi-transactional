# Use the official MySQL image from the Docker Hub
FROM mysql:latest

# Set the environment variables
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=test
ENV MYSQL_USER=username
ENV MYSQL_PASSWORD=password

# Expose the default MySQL port
EXPOSE 3306

# Add the initialization script to the Docker entrypoint
COPY init.sql /docker-entrypoint-initdb.d/

# Start MySQL service
CMD ["mysqld"]
