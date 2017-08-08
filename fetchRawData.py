#!/usr/bin/env python
from urllib import request, parse

def fetchRawData(): 
	sourceURL = 'http://data.taipower.com.tw/opendata01/apply/file/d006001/001.txt'

	req = request.urlopen(sourceURL)
	resp = req.read().decode('utf8')

	return(resp)