import praw

reddit = praw.Reddit(client_id = 'mkfu21NfI--Sjw',
                     client_secret = '-t5X6uSgMTNK-yMj19gq7TXDb_g',
                     username = 'nontoxiccrayon@gmail.com',
                     password = 'scriptsBaby13',
                     user_agent = 'why')



subreddit = reddit.subreddit('memes')

hot = subreddit.hot(limit = 5)

for submission in hot:
    print(submission.title)