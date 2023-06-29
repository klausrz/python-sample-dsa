#!/bin/bash
#docker run -it -w $(pwd) -v $(pwd):$(pwd) python:alpine3.17 ash
docker run -it -w $(pwd) -v $(pwd):$(pwd) python-autoreload ash

# autoreload
# ls heap.py |  entr python heap.py



