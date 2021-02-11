import requests, json, os, sys, csv, pickle, pandas as pd, datetime as dt 
from app.utils.helpers import *
from app.utils.urls import * 
from app.utils.data import *


# Changes in API endpoint render previous iteration worthless. 
# Re-writing entire module.


def get_slate(sportId, *args):
    
get_slate(1)