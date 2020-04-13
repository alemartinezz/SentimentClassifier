# SentimentClassifier

'''
lists of symbols to avoid
'''
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def Strip_punctuation(string):
    '''Return a string without punctuation or symbols'''
    for char in string:
        if char in punctuation_chars:
            string = string.replace(char, '')
    return string


'''
Positive Words
'''
with open("positive_words.txt") as pos_file:
    positive_words = []
    for lin in pos_file:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def Get_pos(phrase):
    '''Get the total number of positive words'''
    phrase = phrase.split(' ')  # split a long string into a list
    # of substrings for being able to iterate over
    total_positive = 0

    for word in phrase:
        word = Strip_punctuation(word)
        word = word.lower()

        if word in positive_words:
            total_positive += 1

    return total_positive


'''
Negative Words
'''
with open("negative_words.txt") as pos_file:
    negative_words = []
    for lin in pos_file:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def Get_neg(phrase):
    '''Get the total number of negative words'''
    phrase = phrase.split(' ')  # split a long string into a list
    # of substrings to iterate over
    total_negative = 0

    for word in phrase:
        word = Strip_punctuation(word)
        word = word.lower()

        if word in negative_words:
            total_negative += 1

    return total_negative


'''
Open csv file (fake generated twitter data)
'''
with open("project_twitter_data.csv", "r") as twitter_data:
    csv_twitter_data = []
    csv_twitter_data = twitter_data.readlines()


def Impact(tweet):
    '''measure the impact of each tweet (check the retweets and replies)'''
    tweet = tweet.split(',')
    number_of_retweets = tweet[-2]
    number_of_replies = tweet[-1]
    # cannot use Strip_punctuation function because it deletes commas
    number_of_replies = number_of_replies.replace('\n', '')
    return number_of_retweets, number_of_replies


def Scores(tweet):
    '''measure the scores of each tweet (count the positive and
    negative words)'''
    tweet = Strip_punctuation(tweet)
    positive_score = Get_pos(tweet)
    negative_score = Get_neg(tweet)
    net_score = positive_score - negative_score
    return positive_score, negative_score, net_score


'''
Write the new file with the analyzed data
'''
outfile = open("resulting_data.csv", "w")
outfile.write('Number of Retweets, Number of Replies, Positive Score, '
              'Negative Score, Net Score')
outfile.write('\n')

for tweet in csv_twitter_data[1:]:
    row_tweet = '{},{},{},{},{}'.format(Impact(tweet)[0], Impact(tweet)[1],
                                        Scores(tweet)[0], Scores(tweet)[1],
                                        Scores(tweet)[2])
    print(row_tweet)
    outfile.write(row_tweet)
    outfile.write('\n')

outfile.close()
