import openai

openai.api_key = ""

f1=open("unfilteredTweets.txt", "r")
tweets=""
tweetList=[]

lines = f1.readlines()
for line in lines:
    tweets=tweets+line
    tweetList.append(line)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Classify the sentiment in these tweets:\n\n\"" + tweets,
  temperature=0,
  max_tokens=1024,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

responses = response.choices[0].text.split("\n")

f2=open("negativeFilteredTweets.txt", "w")
f3=open("positiveFilteredTweets.txt", "w")

count=-2
for responseText in responses:
    if "Negative" in responseText:
        f2.write(tweetList[count])
    elif "Positive" in responseText:
        f3.write(tweetList[count])
    count += 1

f1.close()
f2.close()

print(responses)