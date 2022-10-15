from pathlib import Path
from typing import Optional
from typing import Any
from charticulator import charticulator

import streamlit as st
import pandas as pd;

import utils

import tutorial
import gallery


def main():

    tabTutorial, tabCharts = st.tabs(["🏫 Tutorial", "📈 Charts gallery"])

    with tabCharts:
        gallery.main()

    with tabTutorial:
        tutorial.main()

if __name__ == "__main__":
    main()