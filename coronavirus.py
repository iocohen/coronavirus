from pytrends.request import TrendReq
from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import datetime

now = datetime.datetime.now()


# Get full path for writing.


def get_searches(key_word, state):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(
        [key_word], cat=0, timeframe='2020-02-01 2020-03-12',  gprop='', geo='{}'.format(state))
    df = pytrends.interest_over_time()

    print(df.head())

    sns.set()
    df['timestamp'] = pd.to_datetime(df.index)
    sns.lineplot(df['timestamp'], df[key_word])

    plt.title("THE TREND FOR " + state)
    plt.ylabel("Number of Searches")
    plt.xlabel("Date")
    plt.xticks(rotation=45)
    name = state + str(now) + ".png"
    path = "/Users/ionutcohen/Desktop/coronaVirus/" + name

    plt.savefig(path)
    plt.show()


get_searches('Coronavirus', 'RO')
# get_searches('Coronavirus', 'MA')
# get_searches('Coronavirus', 'CA')
