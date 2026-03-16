# Infrastructure

This project uses Docker to run the core infrastructure.

Current services:

- Elasticsearch → log storage
- Kibana → log visualization

Both services run through docker-compose.

Ports:

- Elasticsearch → 9200
- Kibana → 5601