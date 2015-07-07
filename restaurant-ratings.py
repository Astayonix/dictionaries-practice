
def alpha_ratings(file_name):
    '''
        Parameter: file_name - name of file containing restaurant ratings 
        Returns: None

        alpha_ratings() prints the restaurants in alphabetical order with their associated ratings
    '''

    #open file
    fh = open(file_name)

    #Parse file and create dictionary where the keys are restaurants and the values are ratings
    rest_ratings = {}
    for line in fh:
        rest_name, ratings = line.split(":")
        ratings = ratings.rstrip()
        rest_ratings[rest_name] = ratings
        
    # Sort restaurant names alphabetical

    # Print names and ratings