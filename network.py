# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import random

letter_to_num = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","w","y","z","á","é","í","ó","ú","ü","ñ", "ã"]


# load the dataset

text_file = open("english.txt", "r")
english = text_file.readlines()

text_file = open("spanish.txt", "r")
spanish = text_file.readlines()

# split into input (X) and output (y) variables

temp_set = []

for word in english:
    if len(word) > 15:
        continue
    try:
        word_array = [[0 for num in range(34)] for num1 in range(15)]
        for num, letter in enumerate(word.lower().strip()):
            word_array[num][letter_to_num.index(letter)] = 1
        temp_set.append((word_array, 0))
    except Exception as a:
        print(a)

for word in spanish:
    if len(word) > 15:
        continue
    try:
        word_array = [[0 for num in range(34)] for num1 in range(15)]
        for num, letter in enumerate(word.lower().strip()):
            word_array[num][letter_to_num.index(letter)] = 1
        temp_set.append((word_array, 1))
    except Exception as a:
        #print(a)
        pass

random.shuffle(temp_set)

X = []
Y = []

for item in temp_set:
    X.append(item[0])
    Y.append(item[1])

# define the keras model
model = Sequential()
model.add(Dense(15, input_dim=34, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(3, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, Y, epochs=15, batch_size=10)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
