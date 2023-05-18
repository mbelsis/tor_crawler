# Tor Crawler
<pre>
**Tor Crawler developed by William Solis Guerrero**
</pre>
## Propósito

This software is a web spider or also known as a web crawler, to access, navigate and index the content hosted on the Tor network, and that through web scraping and NLP techniques automatically identifies ONION services related to computer crimes. The discovered and categorized sites are stored in a database, this includes the source of the page, so multimedia content is excepted. The information related to computer crimes is intended to be of high relevance for control agencies or entities in helping to discover activities, habits or behaviors that are the object of analysis and criminal study that result or may result in the mitigation of these criminal acts.
 
### Flujo de Trabajo
 
#### Crawling
 
 1) Storage of seed links to the crawler queue.
     2) Get next site in crawling queue.
     3) Site status check. In the event that the parent domain has already been reviewed and was not online, the same process is avoided for links to its subdomains.
     4) Discovery of new links.
     5) Extraction of the source code of the site.
     6) Store data from the site that is the object of crawling and scraping.
     7) Store new found links to the crawling queue. Links that already exist in the queue will not be stored.
     8) Rerun from step 2.

#### Content Categorization

     1) Get following link and stored content for analysis.
     2) Pre-processing and content preparation.
     3) Obtain possible theme of the site, key terms related to the content.
     4) Categorization of the site by comparison with a crime dictionary.
     5) Store analyzed site, its results and illegal relationship if applicable.
     6) Repeat step 1 again.
## Instrucciones
 
### Dependencias en S.O.

- Tor
- Python 3.x
- Postgres 10

### Dependencias Python

- nltk
- gensim
- bs4
- beautifulsoup4
- polyglot
- validators
- urllib3
- psycopg2
- stem

### Configuración Inicial

It is necessary to have the control port installed and configured in Tor, this can be done through scripttor_install_config.sh 

`chmod -x tor_install_config.sh`

`bash tor_install_config -p 9051 -w your_password`

<pre>
usage: tor_install_config.sh [-p] [-w]

required arguments:
  -p, --port-control    Asigna el puerto de control para Tor, por defecto es 9051.
  -w, --password        Es el password para evitar accesos de terceros no autorizados. 
</pre>

Crear el esquema inicial de la base de datos, ejecutar:

`psql -U user_db -h host_db -f schema_db.sql`

Instalar dependencias de python, ejecutar:

`pip install -r requirements.txt`

### Puesta en Marcha

#### Crawler

To run the crawler it is necessary to have entered the seed links in the `OnionLinkSeed.txt` file and in
`config.properties` the access parameters to the database. Later it will be necessary to execute the following command:

`python main.py -s OnionLinksSeed.txt -c config.properties`

<pre>
usage: main.py [-c] [-s]

required arguments:
  -c, --config-file     Archivo de configuracion de acceso a la base de datos.
  -s, --seed            Archivo que contiene los enlaces semilla. 
</pre>

#### Categorización de sitios

To run the categorization of discovered sites it is necessary to have entered the `crime_keywords.json` file
the key terms of each crime to identify. Later it will be necessary to execute the following command:

`python main_nlp.py -c config.properties -k crime_keywords.json`

<pre>
usage: main_nlp.py [-c] [-k]

required arguments:
  -c, --config-file     Archivo de configuracion de acceso a la base de datos.
  -k, --keywords-file   Archivo que contiene terminos clave para criterios de categorización. 
</pre>
