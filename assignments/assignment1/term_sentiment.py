# Assignment 1, Question 3; Douglas Schumacher, CS 639, February 2019
import sys

def create_sent_dict(sentiment_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

        Args:
            sentiment_file (string): The name of a tab-separated file that contains
                                     all terms and scores (e.g., the AFINN file).

        Returns:
            dicitonary: A dictionary with schema d[term] = score
        """
    afinnfile = open(sentiment_file, 'r')
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t") # The file is tab-delimited and "\t" means tab character
        scores[term] = int(score) # Convert the score to an integer. It was parsed as a string.
    afinnfile.close()
    
    return scores


def get_tweet_sentiment(tweet, sent_scores):
    """A function that find the sentiment of a tweet and outputs a sentiment score.

            Args:
                tweet (string): A clean tweet
                sent_scores (dictionary): The dictionary output by the method create_sent_dict

            Returns:
                score (numeric): The sentiment score of the tweet
        """
    score = 0
    tweet_left = tweet # Copy of tweet that will only hold unscored portions

    # Iterate through sent_scores, only looking at phrases
    for term in sent_scores:
        if len(term.split()) > 1: # Pick out phrases in sent_scores
            if term in tweet_left: # Also removes apostrophe when searching for matches becuase our clean tweets have them removed
                score += sent_scores[term]
                tweet_left = tweet_left.replace(term, '')
    
    # Iterate through sent_scores, only looking at words
    for term in sent_scores:
        if len(term.split()) == 1: # Pick out words in sent_scores
            if term in tweet_left.split(): # Split into individual words, also removes apostrophe when searching for matches becuase our clean tweets have them removed
                score += sent_scores[term]
                tweet_left = tweet_left.replace(term, '')

    return score


def term_sentiment(sent_scores, tweets_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

            Args:
                sent_scores (dictionary): A dictionary with terms and their scores (the output of create_sent_dict)
                tweets_file (string): The name of a txt file that contain the clean tweets
            Returns:
                dicitonary: A dictionary with schema d[new_term] = score
            """
    new_term_sent = {}
    tweets = open(tweets_file, 'r')
    for tweet in tweets:
        score = get_tweet_sentiment(tweet, sent_scores)
        average_score = 0
        if score != 0:
            average_score = (score / len(tweet.split()) * 10) # Weights score  by 10x so that final values are more representative
        tweet_new_words_list = new_terms(sent_scores, tweet)
        for word in tweet_new_words_list:
            if word in new_term_sent:
                old_score = new_term_sent[word]
                new_term_sent[word] = float((old_score * 10 + average_score) / 2) # Takes average of old score and new score and sets as new score
            else:
                new_term_sent[word] = float(average_score)
    tweets.close()

    return new_term_sent


def new_terms(sent_scores, tweet):
    tweet_left = tweet # Copy of tweet that will only hold unscored portions
    # Iterate through sent_scores, only looking at phrases
    for term in sent_scores:
        if len(term.split()) > 1: # Pick out phrases in sent_scores
            if term in tweet_left:
                tweet_left = tweet_left.replace(term, '')
    
    # Iterate through sent_scores, only looking at words
    for term in sent_scores:
        if len(term.split()) == 1: # Pick out words in sent_scores
            if term in tweet_left.split(): # Split into individual words
                tweet_left = tweet_left.replace(term, '')
    return tweet_left.split()


def main():
    sentiment_file = sys.argv[1]
    tweets_file = sys.argv[2]

    # Read the AFINN-111 data into a dictionary
    sent_scores = create_sent_dict(sentiment_file)

    # Derive the sentiment of new terms
    new_term_sent = term_sentiment(sent_scores, tweets_file)

    for term in new_term_sent:        
        print(term, new_term_sent[term])


if __name__ == '__main__':
    main()