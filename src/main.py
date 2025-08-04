from FileHandler import FileHandler
from DataAnalyzer import DataAnalyzer
from ReportBuilder import ReportBuilder


df = FileHandler.get_df("../data/tweets_dataset.csv")
da = DataAnalyzer(df)
rb = ReportBuilder(da)
