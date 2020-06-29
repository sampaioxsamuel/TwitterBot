import praw
import time
import tweepy
import urllib

auth = tweepy.OAuthHandler('XXX', 'XXX')
auth.set_access_token('XXX','XXX')
api = tweepy.API(auth)

reddit = praw.Reddit('bot1', user_agent='bot1 user agent')
subreddit = reddit.subreddit("emo")

def checkConnection():
    page = urllib.request.Request('https://www.reddit.com')
    status_code = True
    try:
        urllib.request.urlopen(page)
    except urllib.error.URLError as err:
        if err.reason:
            status_code = False
    return status_code

def getPost():
    for submission in subreddit.new(limit=None):
        if submission.media:
            send = submission.title + "\n" + submission.url
            break
    return send

def runBot():
    while True:
        try:
            post = getPost()
            api.update_status(status=post)
            print("#"*20)
            print(post)
            time.sleep(60)
        except tweepy.TweepError as error:
            if error.api_code == 187:
                print("#"*20)
                print("Post duplicado")
                time.sleep(300)

def main():
    connection = checkConnection()
    print("#"*20)
    while True:
        if connection:
            print("Iniciando...")
            runBot()
        else:
            print("erro de conexao, tentando novamente")
            time.sleep(60)
