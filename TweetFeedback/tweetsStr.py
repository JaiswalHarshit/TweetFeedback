import snscrape.modules.twitter as sntwitter
import openai

openai.api_key = ""

query = "telestaff"
# limit to stop the process
limit = 50
tweets = []


def pushTweetToFile(tweet, type):
    from datetime import datetime
    dateStr = datetime.today().strftime('%Y-%m-%d')
    f = open("tweets_" + type + "_" + dateStr + ".txt", "a", encoding="utf-8")
    f.write("\n" + tweet)
    f.close()


def fetchTweets():
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            break
        else:
            if tweet.lang == 'en':
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt="Classify the sentiment in these tweets:\n\n\"" + tweet.rawContent,
                    temperature=0,
                    max_tokens=1024,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                )
                responseText = response.choices[0].text
                if "Negative" in responseText:
                    pushTweetToFile(tweet.rawContent, 'negative')
                elif "Positive" in responseText:
                    pushTweetToFile(tweet.rawContent, 'positive')
                elif "Neutral" in responseText:
                    pushTweetToFile(tweet.rawContent, 'neutral')
                tweets.append(tweet.rawContent)


if __name__ == '__main__':
    fetchTweets()
