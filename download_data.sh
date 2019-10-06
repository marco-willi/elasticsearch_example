#!/bin/sh

# Download data to ${HOME}/data

mkdir -p ${HOME}/data
cd ${HOME}/data
#wget 'https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz'
#tar -zxvf aclImdb_v1.tar.gz
wget -O data.csv 'https://dataverse.harvard.edu/api/access/datafile/:persistentId?persistentId=doi:10.7910/DVN/GMFCTR/IZQODZ'
