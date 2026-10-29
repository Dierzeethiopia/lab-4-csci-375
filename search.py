import argparse
import data
import numpy
import gensim.downloader as api
from gensim.models.word2vec import Word2Vec



def cosine(vA, vB):
    ''' Returns the cosine similarity of two numpy ndarray objects. '''
    return numpy.dot(vA, vB) / (numpy.sqrt(numpy.dot(vA,vA)) * numpy.sqrt(numpy.dot(vB,vB)))



def text_vector(text, embeds):
    vec = numpy.zeros(50)
    for word in text.lower().split():
        word = word.strip('.,!?;:"()[]')
        if word in embeds:
            vec = vec + embeds[word]
    return vec



if __name__ == '__main__':
    # Download a pre-trained model   (100,200 also available)
    print('Loading the embeddings...')
    embeds = api.load("glove-twitter-50")  # if you want Twitter-trained embeddings
    
    # Command-line argument parser
    parser = argparse.ArgumentParser(description="search.py")
    parser.add_argument('-data', action="store", dest="data", type=str, default='data', help='Directory containing the tweets subdirectory')
    args = parser.parse_args()


    #
    # YOUR CODE HERE.
    # 

    # Get 100000 tweets.   (you can increase this as you wish!)
    tweets = data.Tweets(args.data).get_tweets(100000)

    # Loop until the user types 'quit'.
    while True:

        # Search query.
        query = input('search: ')

        # if the user enters quites, break
        if query == 'quit':
            break

        query_vec = text_vector(query, embeds)

        if numpy.linalg.norm(query_vec) == 0:
            print("No matching words found")
            continue

        # compare the search with each tweet
        results = []
        for tweet in tweets:
            if tweet is None:
                continue
            tweet_vec = text_vector(tweet, embeds)
            if numpy.linalg.norm(tweet_vec) != 0:
                score = cosine(query_vec, tweet_vec)
                results.append((score, tweet))
                
        # sort from most similar to least similar
        results.sort(reverse=True)


         # print the top 10 tweets
        for score, tweet in results[:10]:
            print(f"{score:.3f}\t{tweet}")