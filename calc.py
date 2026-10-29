import numpy
import gensim.downloader as api

# print("Loading embeddings...")
embeds = api.load("glove-wiki-gigaword-50")


#
# Simple calculator program.
#    1 + 3 + 5 - 3
#

# Initial input.
line = input('calc> ')


while line != 'quit':
    # Initialize variables for new computation.
    X = numpy.zeros(50)
    op = '+'
    parts = line.split()
    valid = True
    
    # Loop over every 2 inputs
    for i in range(0,len(parts),2):
        
        word = parts[i]
        
        # we check if the word exists
        if word not in embeds:
            print(word, "<-- is UNKNOWN Word")
            valid = False
            break
        
        vec = embeds[word]
        
        if op == '+':
            X = X + vec
        elif op == '-':
            X = X - vec
        else:
            print('ERROR: unknown input', op)

        # If we're not at the end of the entire input, grab the operator.
        if i+1 < len(parts):
            op = parts[i+1]

    # The answer!
    
    # we print the two closest words if words are valid
    if valid:
        sims = embeds.similar_by_vector(X)
        print(sims[0][0], sims[1][0])
    
    # New computation to input.
    line = input('calc> ')
