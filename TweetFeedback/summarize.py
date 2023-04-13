import openai

from sendEmail import sendEmail

openai.api_key = ""

f1 = open("tweets.txt", "r")

response1 = openai.Completion.create(
    model="text-davinci-003",
    prompt="Convert my short hand into a first-hand account of the meeting:\n\n" + f1.read(),
    temperature=0,
    max_tokens=1024,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

tweets = response1.choices[0].text

f2 = open("feedback.txt", "r")
feedback = f2.read()

final = tweets + feedback

response2 = openai.Completion.create(
    model="text-davinci-003",
    prompt="Summarize this for a second-grade student:\n\n" + final,
    temperature=0.7,
    max_tokens=1024,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

f1.close()
f2.close()

sendEmail(response2.choices[0].text)

print(response2.choices[0].text)
