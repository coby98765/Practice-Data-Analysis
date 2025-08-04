import pandas as pd
import re

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
        popular_dict = dict()
        #antisemitic
        antisemitic_texts = " ".join(self.df_antisemitic.Text).lower()
        # clean text
        antisemitic_clean_text = DataAnalyzer.clean_text(antisemitic_texts)
        # get most popular words list
        popular_dict["antisemitic"] = DataAnalyzer.find_popular_words(antisemitic_clean_text)

        #non_antisemitic
        non_antisemitic_texts = " ".join(self.df_non_antisemitic.Text).lower()
        # clean text
        non_antisemitic_clean_text = DataAnalyzer.clean_text(non_antisemitic_texts)
        # get most popular words list
        popular_dict["non_antisemitic"] = DataAnalyzer.find_popular_words(non_antisemitic_clean_text)

        #total
        total_texts = " ".join(self.df.Text).lower()
        #clean text
        total_clean_text = DataAnalyzer.clean_text(total_texts)
        #get most popular words list
        popular_dict["total"] = DataAnalyzer.find_popular_words(total_clean_text)

        return popular_dict



    def caps_word_count(self):
        pass

    @staticmethod
    def _longest_text_in_df(df):
        sorted_df = df.sort_values(by='Text',
                                   ascending=False,
                                   key=lambda msg: msg.str.len())
        return sorted_df[:3].to_dict(orient="index")

    @staticmethod
    def clean_text(text):
        keyword = "https://t.co/"
        splited_text = text.split()
        for i in range(len(splited_text)):
            if keyword in splited_text[i]:
                splited_text[i] = ""
        joined_text = " ".join(splited_text)
        clean_text = re.sub(r'[^A-Za-z0-9 ]+', " ", joined_text)
        return clean_text

    @staticmethod
    def find_popular_words(text):
        wordcount = dict()
        for word in text.split():
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
        sorted_words = {k: v for k, v in sorted(wordcount.items(), key=lambda item: item[1])}
        sorted_keys = list(sorted_words.keys())
        return sorted_keys[-10:]

