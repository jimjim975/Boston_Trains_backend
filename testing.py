import re
import datetime as dtt
import psycopg2
import requests
import pandas as pd
from flask import Flask, request,render_template

headers = {'x-api-key' : ''}
response = requests.get("https://api-v3.mbta.com/routes?filter[type]=0,1", headers=headers)
finished = response.json()
lines = []
for items in finished['data']:
    name = items['attributes']['long_name']
    datas = items['attributes']
    lines.append(dict({'name': name, 'endpoint': datas['direction_destinations'], 'directions': datas['direction_names']}))


for items in lines:
    print("\n\n" + str(items))

lines = requests.get("https://api-v3.mbta.com/lines", headers=headers)
finishedlines = response.json()

print(finishedlines)
