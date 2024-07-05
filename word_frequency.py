

if __name__ == '__main__':

    with open('pg16317.txt', "r") as f:
        text = f.read()

    words = text.split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1


    sorted_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
    print("Words ranked from 10th to 20th by frequency:")
    for i in range(9, 19):
        print(sorted_frequency[i][0] + ":", sorted_frequency[i][1])