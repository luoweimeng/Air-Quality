#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()

server.retrieve({
    'stream': "oper",
    'levtype': "sfc",
    'param': "134.128/165.128/166.128/167.128/168.128",
    'dataset': "interim",
    'step': "0",
    'grid': "0.125/0.125",
    'time': "00/06/12/18",
    'date': "2014-01-01/to/2017-12-31",
    'type': "an",
    'class': "ei",
    #N/W/S/E
    'area': "41/115/39/117",
    'format': "netcdf",
    'target': "test.nc"
})



server.retrieve({
    "class": "ei",
    "dataset": "interim",
    "date": "2014-01-01/to/2017-12-31",
    "expver": "1",
    'grid': "0.125/0.125",
    "levelist": "500/850/1000",
    "levtype": "pl",
    "param": "130.128/131.128/132.128/133.128/135.128/155.128/157.128",
    "step": "0",
    "stream": "oper",
    "time": "00:00:00/06:00:00/12:00:00/18:00:00",
    "type": "an",
    "area": "41/115/39/117",
    "format": "netcdf",
    "target": "output.nc",
})