#!/usr/bin/env python

def datetimeFixer(str):
	findStr = '"":"'
	replaceWithStr = '"datetime":"'
	str = str.replace(findStr, replaceWithStr)
	return(str)

def syntaxFixer(sourceData):
	sourceData = datetimeFixer(sourceData)
	return(sourceData)