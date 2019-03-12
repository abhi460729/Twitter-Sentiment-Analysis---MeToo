from textblob import TextBlob #Python library for processing textual data.
import sys, tweepy #Python client for the official twitter API.
import matplotlib.pyplot as plt #Matplotlib is a plotting library in python and matplotlib.pyplot is a collection of command style functions tht make matplotlib work like a MATLAB(better representation).

#Function to calculate the percentage of the desired type of tweets for sentiment analysis.
def percentage(part, whole):
    return 100 * float(part) / float(whole)

#Setting up of twitter API credentials.
#Credentials are obtained by setting up an account at https://apps.twitter.com .
consumerKey = "ukPBWiILI6x6vOGi0ftgC29YY"
consumerSecret = "lU1fSm9wPvF0RBCwKfi5OapuPOZaF6cpcSs8M4r6OkJG4Yy8XE"
accessToken = "744784754453544961-1DOuUu1U9mPATyCk4Rqh1Zihkhrn3LC"
accessTokenSecret = "N7yyU9jWKxBJ4ocMOBmZ7PwzaqQ7Z8fOT5pOOOeHuWqP9"

#Establishing connection with API or Twitter API Authentication.

#Rebuild an OAuth handler with stored access token.
auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret) #Tweepy supports OAuth authentication.auth is OAuthHandler Instance.
auth.set_access_token(accessToken, accessTokenSecret)#Access token is the key for opening the twitter API Treasure Box.

#Now, OAuth Handler instance is equipped with access token.
#Ready for any activity.

api = tweepy.API(auth)#API Instance

#Enter the details from the user that what is the term to be searched and how many tweets are to be analysed.
searchTerm = input("Enter keywork/hashtag to search about: ")
noOfSearchTerms = int(input("Enter how many tweets to analyse: "))

tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)

#Labeling
positive = 0
negative = 0
neutral = 0
polarity = 0

#Traversing through the tweets.
for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity = polarity+analysis.sentiment.polarity #Using TextBlob sentiment.polarity function to store the polarity in the poolarity variable.

    #Calculating the positive, negative and neutral count of the tweets based on the polarity.
    if(analysis.sentiment.polarity == 0):
        neutral =neutral+1
    elif(analysis.sentiment.polarity < 0):
        negative =negative+1
    elif(analysis.sentiment.polarity > 0):
        positive =positive+1


#Calculating the % of the various categories of the labels and polarity.
positive=percentage(positive,noOfSearchTerms)
negative=percentage(negative,noOfSearchTerms)
neutral=percentage(neutral,noOfSearchTerms)
polarity=percentage(polarity,noOfSearchTerms)


positive = format(positive,'.2f')
negative = format(negative,'.2f')
neutral = format(neutral,'.2f')

print("How people are reacting on  "+ searchTerm + " by analyzing "+ str(noOfSearchTerms) + " Tweets.")

#Printing the Polarity.
if(polarity == 0):
    print("Neutral")
elif(polarity<0):
    print("Negative")
elif(polarity>0):
    print("Positive")

#Plotting the Data.
labels=['Positive {'+str(positive)+'%]','Neutral {'+str(neutral)+'%]','Negative {'+str(negative)+'%]']
sizes=[positive,neutral,negative]
colors=['yellowgreen','gold','red']
patches,texts=plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches, labels,loc="best")
plt.title('How people are reacting on '+searchTerm+' by analyzing '+str(noOfSearchTerms)+' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()




