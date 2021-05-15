# System Design

Minitwit is a social media application that provides basic Twitter-like services. It consists of a web app and API services that are publicly available on the internet. Both services allow the user to register a profile, log in, create messages (tweets), follow and unfollow users. Basic authentication is required when creating messages, following, or unfollowing. Most of the application is written in Python, since our web app and API are using the Django framework. 

Minitwit also consists of monitoring tools, which the web app and API communicate with when certain metrics are updated. These tools include Prometheus and Grafana, which allow for collection and displaying of metrics respectively. The monitoring tools are very useful for us developers, since they help us to maintain the system properly. 

For logging features, we have implemented an EFK stack that includes Filebeat, Elastic Search, and Kibana. Filebeat is responsible for harvesting the data that we want to log, while Elastic Search is used to store that data in a database. With the logging features implemented, it is much easier for developers to diagnose and debug problems with the system. It also helps us in maintaining the system.

# Architecture

![Deployment Diagram](images/deployment_diagram.png "Deployment Diagram")

Minitwit is hosted on multiple Digital Ocean droplets which form a Docker Swarm. Our logging and production database are each containerized on their own separate Droplets. This allows us to easily horizontally scale everything besides our persistent data, which should not be horizontally scaled anyways. 

With a project that requires a web app, database, and API, it is normal to have the web app communicate with the database through the API. However, Django is designed such that direct communication with a database backend is much simpler to implement than communication with a custom backend server. For this reason, our web app and API don't communicate with one another, and therefore don't form a frontend/backend structure. Instead, our database is our backend and our web app/API servers are our frontends.

We have a proxy service that uses nginx to route traffic from minitwititu.xyz to our web app server's IP address, and from api.minitwititu.xyz to our API server's address. It only exposes those two IPs, so all of the logging and monitoring related IPs are not exposed.

Our logging is accomplished by our Filebeat service, along with a logging database that hosts an Elastic Search instance. Filebeat scrapes the swarm manager's output, including all standard output for all services in the stack, and then logs relevant data in the logging database (Elastic Search). This logging database is used by Kibana to display our log information in a neat and readable website.

Our monitoring is accomplished by Prometheus, which exposes our metrics on minitwitwitu.xyz/metrics. Our web app and API both make calls to update certain Prometheus metrics, and Prometheus gathers other performance-related metrics from both of them. The /metrics route is also checked by our Grafana service, which hosts a webpage in which metrics can be monitored through customizeable dashboards.


# Dependencies

Our dependencies are split into direct dependencies and tools

## Tools

- Docker | Cloud computing services
- Digital Ocean | Cloud infrastructure provider
- Travis | Hosted continuous integration service
- ElasticSearch | Distributed RESTful search and analytics engine
- Kibana | Data visualization dashboard software for ElasticSearch
- Filebeat | File harvester
- PostGreSQL | Database Manangement System
- NGINX | (Web Server used for reverse proxy)

- Flake8 | Python style consistency
- Black | Python code formatter
- SonarQube | Code quality inspector, bugs, vulnerabilities
- Code Climate | Test coverage
- Better Code Hub | Quality improvements

**why nginx, so we dont have ssl cetificate https?? lying around.. så de ikke centraliced managemant of ssl certicifacte.**

## ...??

Web App dependencies are as follows:

- asgiref 3.3.1 - Includes pytest a framework that makes it easy to write small tests
- django 3.1.8 - Python Web Framework
- django-prometheus 2.1.0 - Export django monitoring metrics for Prometheus
- django-rest-framework 3.12.2 - Web APIs for Django
- prometheus 0.9.0 - Prometheus instrumentation library
- psutil 5.8.0 - Python system monitoring
- psycopg2 2.8.6 - PostgreSQL database adapter for Python
- pycodestyle 2.7.0 - Python style checker
- pytz 2021.1 - Cross platform timezone calculations
- requests 2.25.1 - HTTP library
- sqlparse 0.4.1 - SQL query parser / transformer
- uWSGI 2.0.18 - 2.1 - Web service gateway

API dependecies are as follows:

- asgiref 3.3.1 - Includes pytest a framework that makes it easy to write small tests
- django 3.1.8 | Python Web Framework
- django-prometheus 2.1.0 - Export django monitoring metrics for Prometheus 
- markupsafe 1.1.1 - Safely add untrusted strings to HTML/XML markup
- psutil 5.8.0 - Python system monitoring
- psycopg2 2.8.6 - PostgreSQL database adapter for Python
- pytz 2021.1 - Cross platform timezone calculations
- requests 2.25.1 - HTTP library
- sqlparse 0.4.1 - SQL query parser / transformer
- toml 0.10.2 - Python library for TOML
- uWSGI 2.0.18 - 2.1 - Web service gateway
- wrapt 1.12.1 - A Python module for decorators, wrappers and monkey patching.

# Current state

Get the fucking grafana to tell us something xD

# License

We collected all the license for every dependency we have to form the license our product. Here we met the GNU GPL v2 for psycopg2, The GPL series are all copyleft licenses, which means that any derivative work must be distributed under the same or equivalent license terms. To cover the product we therefore chose to go with the GNU General Public License v3.0; can be found in the licence document. In this process we also collected all copyright noticies for the dependencies, these are all placed in the Notice document.