# population

Prerequisites:

https://radanalytics.io/get-started

https://github.com/pshakari/population-data-loader.git
 
This is the app that calls a postgresql db to draw a bar chart of the population of the world:


```sh
oc new-app --template=oshinko-python-spark-build-dc \
  -p APPLICATION_NAME=population \
  -p GIT_URI=https://github.com/pshakari/population.git \
  -p SPARK_OPTIONS='--packages org.postgresql:postgresql:42.1.4' \
  -p OSHINKO_CLUSTER_NAME=spark_oshinko_cluster \
  -e SERVER=postgresql \
  -e DBNAME=populationDb \
  -e PASSWORD=password \
  -e USER=username
  ```
