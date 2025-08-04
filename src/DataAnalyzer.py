import pandas as pd

class DataAnalyzer:
    def __init__(self,df):
        self.df = df
        self.df_antisemitic = self.split_df(1)
        self.df_non_antisemitic = self.split_df(0)

    def split_df(self,val):
        filtered = self.df.where(self.df["Biased"]==val)
        clean_df = filtered.dropna()
        return clean_df

    def count_tweets(self):
        count_dict = self.df["Biased"].value_counts().to_dict()
        count_dict["total"] = len(self.df)
        return count_dict

    def longest_tweets(self):
        len_dict = dict()
        len_dict["antisemitic"] = DataAnalyzer._longest_text_in_df(self.df_antisemitic)
        len_dict["non_antisemitic"] = DataAnalyzer._longest_text_in_df(self.df_non_antisemitic)
        len_dict["total"] = DataAnalyzer._longest_text_in_df(self.df)
        return len_dict

    def most_popular_words(self):
        pass

    def caps_word_count(self):
        pass

    @staticmethod
    def _longest_text_in_df(df):
        sorted_df = df.sort_values(by='Text',
                                   ascending=False,
                                   key=lambda msg: msg.str.len())
        return sorted_df[:3].to_dict(orient="index")
