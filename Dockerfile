FROM alpine:3.1

WORKDIR /

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask

# Bundle app source
COPY app.py app.py
COPY templates/chart.html templates/chart.html
COPY static/Chart.min.js static/Chart.min.js

EXPOSE  8000
CMD ["python", "app.py", "-p 8000"]

