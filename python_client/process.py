""" Process News Articles """
import os
import csv

from datetime import datetime
import time
from elasticsearch import Elasticsearch

# Parameters
data_path = '/data/'
host = 'elasticsearch:9200'

# connect to EL
es = Elasticsearch([host])


# convert timestamp to datetime
def ts2datetime(ts):
    return datetime.strptime(ts[0:10], '%Y/%m/%d')


# Read news articles from disk
articles = list()
with open(data_path + 'data.csv', 'r', encoding='latin-1') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = next(reader)
    for row in reader:
        doc = {h: r for h, r in zip(header, row) if h is not ''}
        # some articles have no valid publish date - we skip these
        try:
            doc['publish_date'] = ts2datetime(doc['publish_date'])
            articles.append(doc)
        except ValueError:
            pass


# create index
es.indices.create(index='doc-index')


# Put news articles into Elasticsearch
for i, article in enumerate(articles):
    res = es.create(index="doc-index", doc_type='news_article',
                    id=i, body=article)
    if (i % 500) == 0:
        print("Processed {} articles".format(i+1))


es.indices.refresh(index="doc-index")

print("Finished inserting data")
