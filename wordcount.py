def count_words(file_name):
    """
        Input: file name - string with file path name 
        Output: Print to stdout the words in the file and the number of times each one occurs

        count_words() iterates over the words in a file and counts how many time each word 
        occurs. The function then prints this info to stdout. The function returns None.
    """
    #Open a file
    text = open(file_name)

    word_count = {}

    #Count how many times each space-separated word occurs in the file
    for line in text:
        words = line.split(" ")
        for word in words:
            # If the word is already in word_count, increment count
            # If the word is not in word_count, initialize the key value pair with value of 1
            word_count[word.rstrip()] = word_count.get(word, 0) + 1

    #Print word counts to stdout
    for w, n in word_count.iteritems():
        print "%s %d" % (w, n)



count_words('twain.txt')