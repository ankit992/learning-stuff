print('How many cats do you have?');
numCats = input();
try:
    if int(numCats) >= 4:
        print('That is a lot of cats');
    else:
        print('That is not many cats');
except ValueError:
    print("you did not enter a number");