import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data(year):
    df = pd.read_csv('tmdb-movies.csv')
    df = df[df['release_year'] == year]
    return df


def bestselling_movie(df):
    """
    Return the name of the best-selling movie and its total revenue

    @param df: pd.DataFrame
    @return: (str, int)
    """
    max_revenue = df['revenue'].mode()[0]
    name = df[df['revenue'] == max_revenue]['original_title']
    return name, max_revenue


def bestselling_director(df):
    """
    Return the name of the bestselling director

    @param df: pd.DataFrame
    @return: str
    """
    max_revenue = df['revenue'].mode()[0]
    name = df[df['revenue'] == max_revenue]['director']
    return name


def relationship_between_revenue_and_budget(df):
    """
    Draw a line graph with budget as x variable and revenue the y variable
    @param df: pd.DataFrame
    @return: the line graph
    """
    plt.draw()

def popularity_and_budget():
    """
    Draw a line graph with budget as x variable and popularity the y variable
    :return:
    """


def main():
    print('Calculating statistics for TMDB')


if __name__ == '__main__':
    main()
