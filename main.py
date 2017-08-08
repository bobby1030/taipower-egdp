#!/usr/bin/env python
from fetchRawData import fetchRawData
from syntaxFixer import syntaxFixer
from contentProcessor import contentProcessor

res = fetchRawData()
res = syntaxFixer(res)
res = contentProcessor(res)

print(res)