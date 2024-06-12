#!/usr/bin/env python3
'''format logs using regex'''
import re
from typing import List
import logging
import os
import mysql.connector
from mysql.connector import MySQLConnection

def filter_datum(fields: List[str], redaction: str, message: str, separator: str)->str:
    '''filter a log message'''
    #search for the field pattern in the message
    for field in fields:
        pat = re.compile(f'{field}=(.*?){separator}')
        match = pat.search(message)
        if match:
            message = re.sub(match.group(1), redaction, message)
    return message

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''inits the format of the logs'''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''formats and redacts the logs'''
        NotImplementedError
        record = super().format(record)
        record = str(record)
        message = filter_datum(self.fields, self.REDACTION, record, self.SEPARATOR)
        return message

def get_logger()->logging.Logger:
    log = logging.Logger('user_data', logging.INFO)
    log.propagate = False
    stream_H = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_H.setFormatter(formatter)
    log.addHandler(stream_H)
    return log

PII_FIELDS = ('name','email','phone','password','ip')


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Creates a connector to a database.
    """
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME", "")
    db_user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_pwd = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    connection = mysql.connector.connect(
        host=db_host,
        port=3306,
        user=db_user,
        password=db_pwd,
        database=db_name,
    )
    return connection
