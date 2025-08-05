class Report:
    def __init__(self):
        self.total_tweets = dict()
        self.average_length = dict()
        self.common_words = dict()
        self.longest_3_tweets = dict()
        self.uppercase_words = dict()

    def set_total_tweets(self,data):
        total_dict = dict()
        total_dict["antisemitic"] = data[1]
        total_dict["non_antisemitic"] = data[0]
        total_dict["total"] = data["total"]
        sub_total = total_dict["antisemitic"] + total_dict["non_antisemitic"]
        total_dict["<unspecified>"] =  data["total"] - sub_total
        self.total_tweets = total_dict

    def set_average_length(self,data):
        average_len_dict = dict()
        average_len_dict["antisemitic"] = data["antisemitic"]
        average_len_dict["non_antisemitic"] = data["non_antisemitic"]
        average_len_dict["total"] = data["total"]
        self.average_length = average_len_dict

    def set_common_words(self,data):
        common_words_dict = dict()
        common_words_dict["antisemitic"] = data["antisemitic"]
        common_words_dict["non_antisemitic"] = data["non_antisemitic"]
        common_words_dict["total"] = data["total"]
        self.common_words = common_words_dict

    def set_longest_tweets(self,data):
        longest_tweets_dict = dict()
        longest_tweets_dict["antisemitic"] = data["antisemitic"]
        longest_tweets_dict["non_antisemitic"] = data["non_antisemitic"]
        longest_tweets_dict["total"] = data["total"]
        self.longest_3_tweets = longest_tweets_dict

    def set_uppercase_words(self,data):
        uppercase_dict = dict()
        uppercase_dict["antisemitic"] = data["antisemitic"]
        uppercase_dict["non_antisemitic"] = data["non_antisemitic"]
        uppercase_dict["total"] = data["total"]
        self.uppercase_words = uppercase_dict

    def to_dict(self):
        report = {
            "total_tweets" : self.total_tweets,
            "average_length": self.average_length,
            "common_words": self.common_words,
            "longest_3_tweets": self.longest_3_tweets,
            "uppercase_words": self.uppercase_words,
        }
        return report