# Assignment 1, Question 2; Douglas Schumacher, CS 639, February 2019
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
            if term in tweet_left.split(): # Split into individual words, also removes apostrophe when searching for matches because our clean tweets have them removed
                score += sent_scores[term]
                tweet_left = tweet_left.replace(term, '')

    return score


def get_sentiment(tweets_file, sent_scores, output_file):
    """A function that finds the sentiment of each tweet and outputs a sentiment score (one per line).

            Args:
                tweets_file (string): The name of the file containing the clean tweets
                sent_scores (dictionary): The dictionary output by the method create_sent_dict
                output_file (string): The name of the file where the output will be written

            Returns:
                None
    """
    tweets = open(tweets_file, 'r')
    output = open(output_file, 'w')
    for tweet in tweets:
        score = get_tweet_sentiment(tweet, sent_scores)
        output.write('%d\n' % score)
    output.close()
    tweets.close()


def main():
    sentiment_file = sys.argv[1]
    tweets_file = sys.argv[2]
    output_file = "sentiment.txt"

    # Read the AFINN-111 data into a dictionary
    sent_scores = create_sent_dict(sentiment_file)
    # Read the tweet data and assign sentiment
    get_sentiment(tweets_file, sent_scores, output_file)


if __name__ == '__main__':
    main()