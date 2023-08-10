# Minimal Python REST API with Flask

A small REST API GET request example in Python with the Fask Framework. The main GET request determines whether a supplied point (consisting out of a longitude and a latitude value) is within the space of a polygon within a geojson.

GEOJSON data from:
https://cartographyvectors.com/map/1011-romania-detailed-boundary

## Setup

1. Create environment and install packages:

    `` conda create -n pyto-apy python=3.10``

    `` conda activate pyto-apy``

    `` conda install``

2. Start the application:

    ``flask run``