#!/usr/bin/env python
# -*- coding: utf-8 -*-


HAS_FUTURES = True
HAS_JOBLIB = False
SHOW_GRAPHICS = True
HAS_MONGODB = True

import os

if HAS_MONGODB:
    import pymongo
import pickle

if os.name == 'nt':
    MONGO_URL = r'mongodb://127.0.0.1:27017'

if HAS_FUTURES:
    import concurrent.futures

if HAS_JOBLIB:
    from joblib import Parallel, delayed
    import multiprocessing
    num_cores = multiprocessing.cpu_count()

def setup_db():
    if job.HAS_MONGODB:
        client = pymongo.MongoClient(job.MONGO_URL)
        lsst = client.lsst
        stars = lsst.stars
        return stars
    else:
        return None


if __name__ == '__main__':
    pass