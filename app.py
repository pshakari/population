import os
from os import environ
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from flask import Markup
from flask import Flask
from flask import render_template

app = Flask(__name__)

class Generator:
    populationSum = []
    continents = []
    
    def __init__(self):
        server = environ.get("SERVER")
        user = environ.get("USER")
        password = environ.get("PASSWORD")
        dbname = environ.get("DBNAME")
        self.make(server,
                  user, dbname, password)

    def make(self, server, user, dbname, password):
        spark_session = SparkSession.builder.appName('population').getOrCreate()
        url = "jdbc:postgresql://{0}/{1}?user={2}&password={3}".format(server, dbname, user, password)
        df = spark_session.read.format("jdbc").options(url=url,dbtable="population",driver="org.postgresql.Driver").load()
        table = df.groupBy('Continent').sum('Population').withColumnRenamed("sum(Population)", "Population").orderBy('Population', ascending=False)
        self.populationSum=[int(row['Population']) for row in table.collect()]
        self.continents=[str(row['Continent']) for row in table.collect()]

@app.route('/')
def index():
    gen = Generator()
    return render_template('chart.html', values=gen.populationSum, labels=gen.continents)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
