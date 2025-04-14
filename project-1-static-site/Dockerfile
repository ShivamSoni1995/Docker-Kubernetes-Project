# Use an official Nginx image as the base image
FROM nginx:alpine

# Copy the static HTML file from your project folder into the Nginx web server directory inside the container
COPY index.html /usr/share/nginx/html/index.html
COPY styles.css /usr/share/nginx/html/styles.css
COPY scripts.js /usr/share/nginx/html/scripts.js


# (Optional) Expose port 80 (Nginx default port) - mainly for documentation
EXPOSE 80
