import snscrape.modules.twitter as sntwitter
import pandas as pd

kelime="DEVA"
tweets=[]
limit=1000

for tweet in sntwitter.TwitterSearchScraper(kelime).get_items():
    if len(tweets)==limit:
        break
    else:
        tweets.append([tweet.date,tweet.user.username,tweet.content])

veri=pd.DataFrame(tweets,columns=["Tarih","Kullanıcı","Tweet"])

date_columns = veri.select_dtypes(include=['datetime64[ns, UTC]']).columns
for date_columns in date_columns:
    veri[date_columns] = veri[date_columns].dt.date

veri.to_csv("C:/Users/selim/Documents/python_projects/tweets.cvs",index=False)
