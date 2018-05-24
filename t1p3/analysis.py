import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    return pd.read_csv('tmdb-movies.csv')


def bestselling_movie(df, year):
    """
    Return the name of the best-selling movie and its total revenue

    @param df: pd.DataFrame
    @param year: str
    @return: (str, int)
    """


def bestselling_director(df):
    """
    Return the name of the bestselling director

    @param df: pd.DataFrame
    @return: str
    """


def relationship_between_revenue_and_budget(df):
    """
    Draw a line graph with budget as x variable and revenue the y variable
    @param df: pd.DataFrame
    @return: the line graph
    """


def popularity_and_budget():
    """
    Draw a line graph with budget as x variable and popularity the y variable
    :return:
    """


def main():
    print('Calculating statistics for TMDB')


if __name__ == '__main__':
    main()