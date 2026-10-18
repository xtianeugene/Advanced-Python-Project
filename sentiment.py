from textblob import TextBlob

def sentiment(text):
    s = TextBlob(text).sentiment.polarity
    return "positive" if s > 0 else "negative" if s < 0 else "neutral"

if __name__=="__main__":
    print(sentiment(input("Text: ")))