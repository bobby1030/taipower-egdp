#!/usr/bin/env python

def datetimeFixer(str):
	str = str.replace('"":"', '"datetime":"')
	return(str)

def keyRenamer(str):
	str = str.replace('aaData', 'data')
	return(str)

def syntaxFixer(sourceData):
	sourceData = datetimeFixer(sourceData)
	sourceData = keyRenamer(sourceData)
	return(sourceData)