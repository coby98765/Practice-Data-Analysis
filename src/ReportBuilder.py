from models.Report import Report
from FileHandler import FileHandler


class ReportBuilder:
    def __init__(self,da):
        self.report = Report()
        self.DataAnalyzer = da

        self.report.set_total_tweets(self.DataAnalyzer.count_tweets())
        self.report.set_common_words(self.DataAnalyzer.most_popular_words())
        self.report.set_uppercase_words(self.DataAnalyzer.caps_word_count())

        FileHandler.export_json(self.report.to_dict())