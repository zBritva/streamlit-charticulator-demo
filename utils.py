from pathlib import Path
from typing import Optional
from typing import Any
from charticulator import charticulator

import streamlit as st

import pandas as pd;

def columns(col):
    return {
        "name": col,
        "displayName": col,
        "type": "string",
    }

def row(row, columns):
    r = {}

    for index, col in enumerate(columns):
        r[col] = row[1][col]

    return r


def convertData(table):
        # create list of columns for charticulator dataset
    columnsList = list(map(columns, table.columns))
    # data rows
    rowsList = list(map(lambda r: row(r, table.columns), table.iterrows()))

    return (columnsList, rowsList)

