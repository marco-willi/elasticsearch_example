# Analyze News-Articles with Elasticsearch

This is a small example to test the process of using Elasticsearch on a small dataset of news articles. 

## Installation

1. Clone the GitHub repo

   
2. Install Docker and Docker-Compose

```shell
chmod +x install_docker.sh
./install_docker.sh
```

3. Download the news articles

```shell
chmod +x download_data.sh
./download_data.sh
```
   

4. Build and run the containers
   
``` shell
sudo docker-compose up --build
```

5. Port-Forwarding to access via Browser (if connecting to a remote host)

``` shell
9200:localhost:9200
5601:localhost:5601
```

## Viewing Articles via Elasticsearch

1. View the ES cluster: 

```
http://localhost:9200
```

2. Look at the created documents: 

```
http://localhost:9200/doc-index/_search
```

## Viewing Articles via Kibana

1. Open Kibana

```shell
http://localhost:5601/app/kibana
```

2. Click on 'Connect to your Elasticsearch index'
3. Define index pattern 'doc-index*'
4. Analyse your data!


## Acknowledgements

The dataset is from:

```
@data{DVN/GMFCTR_2017,
author = {dai, tianru},
publisher = {Harvard Dataverse},
title = "{News Articles}",
year = {2017},
version = {V1},
doi = {10.7910/DVN/GMFCTR},
url = {https://doi.org/10.7910/DVN/GMFCTR}
}
```