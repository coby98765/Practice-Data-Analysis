from abc import abstractmethod

import pandas as pd

class DataAnalyzer:
    def __init__(self,df):
        self.df = df
        self.df_antisemitic = self.split_df(self.df,1)
        self.df_non_antisemitic = self.split_df(self.df,0)

    @staticmethod
    def split_df(df,val):
        mask = df.where(df["Biased"]==val)
        new_df = df[mask]
        return new_df

    def count_tweets(self):

        pass

    def tweets_len(self):
        pass

    def longest_tweets(self):
        pass

    def most_popular_words(self):
        pass

    def caps_word_count(self):
        pass