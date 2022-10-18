from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

def word_cloud(file):
    data = pd.read_csv(file)
    print(data.head())
    text = " ".join(i for i in data.Country) #add column name of your choice
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    plt.figure( figsize=(15,10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

if __name__=="__main__":
    file = r"countries.csv"
    word_cloud(file)