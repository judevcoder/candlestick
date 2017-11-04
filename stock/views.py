# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Stockdata
import pandas as pd
import sqlite3
import datetime
import simplejson
import json
from django.shortcuts import render_to_response
import time
# Create your views here.

def index(request):

    if request.method == 'GET':
        con = sqlite3.connect("db.sqlite3")
        df = pd.read_sql("SELECT * from stockdata", con)

        return render_to_response('stock/index.html')

def stockdata(request):
    if request.method == 'GET':
        stock_data = []
        con = sqlite3.connect("db.sqlite3")
        df = pd.read_sql("SELECT * from stockdata", con)

        for idx, val in enumerate(list(df['underlying_symbol'])):
            if val == 'AMZN':
                date = list(df['quote_date'])[idx]
                # timestamp = time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").timetuple())
                open = list(df['open'])[idx]
                high = list(df['high'])[idx]
                low = list(df['low'])[idx]
                close = list(df['close'])[idx]
                data = [date, open, high, low, close]
                stock_data.append(data)
    return HttpResponse(json.dumps(stock_data), content_type="application/json")
