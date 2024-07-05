if __name__ == '__main__':

    with open('pg16317.txt', "r") as f:
        text = f.read()

    # Split the text into words
    words = text.split()
    word_frequency = {}

    # Calculate the frequency of each word
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    # Sort the words by frequency in descending order
    sorted_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
    print("Words ranked from 10th to 20th by frequency:")
    for i in range(9, 19):
        print(sorted_frequency[i][0] + ":", sorted_frequency[i][1])