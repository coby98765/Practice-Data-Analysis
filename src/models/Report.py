class Report:
    def __init__(self):
        self.total_tweets = dict()
        self.average_length = dict()
        self.longest_3_tweets = dict()
        self.uppercase_words = dict()

    def set_total_tweets(self, data,count):
        total_dict = dict()
        total_dict["antisemitic"] = data["1"]
        total_dict["non_antisemitic"] = data["0"]
        total_dict["total"] = count
        sub_total = total_dict["antisemitic"] + total_dict["non_antisemitic"]
        total_dict["<unspecified>"] = count - sub_total
        self.total_tweets = total_dict


    def to_dict(self):
        report = {
            "total_tweets" : self.total_tweets,
            "average_length": self.average_length,
            "longest_3_tweets": self.longest_3_tweets,
            "uppercase_words": self.uppercase_words,
        }
        return report