#!/usr/bin/env python3
'''format logs using regex'''
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str)->str:
    '''filter a log message'''
    #search for the field pattern in the message
    for field in fields:
        pat = re.compile(f'{field}=(.*?){separator}')
        message = pat.sub(f'{field}={redaction}{separator}', message)
    return message