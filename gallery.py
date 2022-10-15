from pathlib import Path
from typing import Optional
from typing import Any
from charticulator import charticulator

import streamlit as st
import pandas as pd;

import utils


def drawChart(data, tableName,tmplt):

    population = pd.read_csv(data)

    bubble_chart = open(tmplt, 'r').read();
    
    populationTable = utils.convertData(population)

    populationTableDataset = [{
        "name": tableName,
        "displayName": tableName,
        "columns": populationTable[0],
        "rows": populationTable[1],
        "type": "main" # main table
    }];

    bubble_chart_instance = charticulator(
            bubble_chart,
            populationTableDataset,
            {}
    )

def main():
    st.write("## Chart Tempaltes")
    st.write('Templates examples from https://charticulator.com/templates.html')
    
    drawChart(
        "./data/oecd_population_2018.csv",
        "oecd_population_2018",
        './templates/bubble_chart.tmplt'
    )

    drawChart(
        "./data/gapminder.csv",
        "gapminder",
        './templates/scatterplot.tmplt'
    )

    drawChart(
        "./data/driving_trends.csv",
        "driving_trends",
        './templates/connected_scatterplot.tmplt'
    )

    drawChart(
        "./data/oecd_population_2018.csv",
        "oecd_population_2018",
        './templates/lollipop_chart.tmplt'
    )

    drawChart(
        "./data/g7_unemployment_gender_gap.csv",
        "g7_gender_gap_unemployment",
        './templates/dumbbell_chart.tmplt',
    )

    drawChart(
        "./data/co2_emission_ranking.csv",
        "co2_emission_ranking",
        './templates/bump_chart.tmplt'
    )

    # drawChart(
    #     "./data/steps_by_month.csv",
    #     "steps_by_month",
    #     './templates/peacock_chart.tmplt'
    # )

    drawChart(
        "./data/nightingale.csv",
        "nightingale",
        './templates/nightingale_chart.tmplt'
    )

    drawChart(
        "./data/boston_weather_2015.csv",
        "boston_weather_2015",
        './templates/weather_radial_chart.tmplt'
    )

    drawChart(
        "./data/food_supply_per_capita_2013.csv",
        "food_supply_per_capita_2013",
        './templates/marimekko_chart.tmplt'
    )

    drawChart(
        "./data/world_population_2017.csv",
        "world_population_2017",
        './templates/diverging_bar_chart.tmplt'
    )

    drawChart(
        "./data/oecd_mean_median_income.csv",
        "oecd_mean_median_income",
        './templates/nested_bar_chart.tmplt'
    )

    drawChart(
        "./data/september_weather.csv",
        "fake_weather",
        './templates/pictogram.tmplt'
    )

    drawChart(
        "./data/polio_incidence_rates_us.csv",
        "polio_incidence_rates_united_states",
        './templates/heatmap.tmplt'
    )

    drawChart(
        "./data/mobile_os_market_share_jul2021.csv",
        "mobile_os_market_share_jul2021",
        './templates/waffle_chart.tmplt'
    )



if __name__ == "__main__":
    main()
