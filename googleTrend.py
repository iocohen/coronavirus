from pytrends.request import TrendReq
from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import datetime
import sys
import os
import argparse
import pathlib
import uuid

now = datetime.datetime.now()

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required=True, help="insert your word")

ap.add_argument("-c", "--country", required=False, help="country to search on")

args = ap.parse_args()

key_word = args.query
country = args.country
day = '2020-02-01 ' + datetime.datetime.today().strftime('%Y-%m-%d')

pytrends = TrendReq(hl='en-US', tz=360)
pytrends.build_payload(
    [key_word], cat=0, timeframe=day,  gprop='', geo=country)
df = pytrends.interest_over_time()

print(df.head())

sns.set()
df['timestamp'] = pd.to_datetime(df.index)
sns.lineplot(df['timestamp'], df[key_word])
if country == "":
    plt.title("THE Global TREND OF " + key_word)
else:
    plt.title("THE TREND FOR " + country)
plt.ylabel("Number of Searches of " + key_word)
plt.xlabel("Date")
plt.xticks(rotation=45)
uniq_filename = str(datetime.datetime.now().date())

unique_filename = str(uuid.uuid4())

if country == "":
    name = "Worldwide" + uniq_filename + ".png"
else:
    name = country + uniq_filename + ".png"


filepath = pathlib.Path(__file__).resolve().parent

path = os.path.join(filepath, name)

plt.savefig(path)
plt.show()
