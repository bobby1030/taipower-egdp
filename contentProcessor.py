#!/usr/bin/env python
import json
import re
import html

def convertJsonToPythonObject(jsonstr):
	result = json.loads(jsonstr)
	return(result)

def generatorTypeCleaner(source):
	for generators in source['data']:
		generators[0] = re.search('\'(.*)\'', generators[0]).group(1) # generatorType
	return(source)

def generatorTypeSumRemover(source):
	def fn(x):
		if x[1] != '小計':
			return True
		else:
			return None
	
	source['data'] = list(filter(fn, source['data']))
	return(source)

def generatorNameHtmlEntityUnescaper(source):
	for generators in source['data']:
		generators[1] = html.unescape(generators[1])
	return(source)

def generatorNameNotesRemover(source):
	for generators in source['data']:
		generators[1] = re.sub('\(註\d*\)', '', generators[1])
	return(source)

def contentProcessor(sourceData):
	processingData = convertJsonToPythonObject(sourceData)
	processingData = generatorTypeCleaner(processingData)
	processingData = generatorTypeSumRemover(processingData)
	processingData = generatorNameHtmlEntityUnescaper(processingData)
	processingData = generatorNameNotesRemover(processingData)
	result = json.dumps(processingData, ensure_ascii=False) ## convert Python Objects to JSON
	return(result)