# __Systems and Methods for Big and Unstructured Data project__
This project has been developed for the "Systems and Methods for Big and Unstructured Data" course, attended during my Master of Science (A.Y. 2021/22) at the Polytechnic University of Milan. Final grade achieved: 31.5/33.

## Description
Aim of this project was to build an information system for managing pandemic information. In particular, different NoSQL databases have been designed and implemented to support a contact tracing application, a certification app and a data analysis system over data about COVID-19 vaccination statistics. The technologies used have been Neo4J, MongoDB and ElasticSearch, respectively.


## Graph databases
The aim of the first assignment was to trace contacts between people, to monitor the viral diffusion. In order to do so, it was needed to design, store, and query a graph data structure in Neo4J for supporting a contact tracing application for COVID-19.

The [Neo4J](/neo4j_assignment) assignment directory is organized in the following way:
- The [Neo4J database populator](/neo4j_assignment/neo4jDB-populator/) folder contains the package responsible for the automatic population of the graph database
- In the [GUI](/neo4j_assignment/GUI/) folder there is the package containing all the necessary classes to run the python application supported by the Neo4j database
- The [deliverables](/neo4j_assignment/deliverables/) folder contains the pdf report file and some example queries


## Document-oriented databases
The aim of the second assignment was to design, store and query data on MongoDB supporting a certification app for COVID-19. The data storage solution had to keep track of people and information about their tests and vaccination status. In particular, it was required to record in a document-based storage the certificate of vaccination/testing and the authorized bodies that can deliver them.

The [MongoDB](/MongoDB_assignment) assignment directory is organized in the following way:
- The [data](/MongoDB_assignment/data/) folder contains the main.py file used to populate the document oriented DB, the webapp package containing all the necessary files to run the webapp application supported by the MongoDB database and a queries and commands file listing some examples of MongoDB queries
- In [report](/MongoDB_assignment/Report/) folder the pdf report of the assignment is contained


## Information-retrieval databases
The aim of the last assignment was to design, store and query data on ElasticSearch supporting a data analysis scenario over data about COVID-19 vaccination statistics. The purpose was that of building a comprehensive database of vaccinations. It was suggested to get and import the dataset available as open data at the following [link](https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv).

The [ElasticSearch](/ElasticSearch_assignment) assignment directory contains the following elements:
- The dashboard file which can be imported in Kibana to visualize it
- The queries file containing a list of example queries for the ElasticSearch database
- The dataset cleaner and merge dataset python files, used to fix some format code in the csv file
- In the [report](/ElasticSearch_assignment/Report/) folder the pdf report of the assignment is contained
