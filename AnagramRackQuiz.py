import sys
import random


def step(start, end, step):
    while start <= end:
        yield start
        start += step


letters = [
    'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
    'B', 'B',
    'C', 'C',
    'D', 'D', 'D', 'D',
    'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E',
    'F', 'F',
    'G', 'G', 'G',
    'H', 'H',
    'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I',
    'J',
    'K',
    'L', 'L', 'L', 'L',
    'M', 'M',
    'N', 'N', 'N', 'N', 'N', 'N',
    'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
    'P', 'P',
    'Q',
    'R', 'R', 'R', 'R', 'R', 'R',
    'S', 'S', 'S', 'S',
    'T', 'T', 'T', 'T', 'T', 'T',
    'U', 'U', 'U', 'U',
    'V', 'V',
    'W', 'W',
    'X',
    'Y', 'Y',
    'Z',
    '?', '?'
]

twos = [
    ["AA"],
    ["AB"],
    ["AD"],
    ["AE"],
    ["AG"],
    ["AH"],
    ["AI"],
    ["AL"],
    ["AM"],
    ["AN"],
    ["AR"],
    ["AS"],
    ["AT"],
    ["AW"],
    ["AX"],
    ["AY"],
    ["BA"],
    ["BE"],
    ["BI"],
    ["BO"],
    ["BY"],
    ["DA"],
    ["DE"],
    ["DO"],
    ["ED"],
    ["EF"],
    ["EH"],
    ["EL"],
    ["EM"],
    ["EN"],
    ["ER"],
    ["ES"],
    ["ET"],
    ["EW"],
    ["EX"],
    ["FA"],
    ["FE"],
    ["GI"],
    ["GO"],
    ["HA"],
    ["HE"],
    ["HI"],
    ["HM"],
    ["HO"],
    ["ID"],
    ["IF"],
    ["IN"],
    ["IS"],
    ["IT"],
    ["JO"],
    ["KA"],
    ["KI"],
    ["LA"],
    ["LI"],
    ["LO"],
    ["MA"],
    ["ME"],
    ["MI"],
    ["MM"],
    ["MO"],
    ["MU"],
    ["MY"],
    ["NA"],
    ["NE"],
    ["NO"],
    ["NU"],
    ["OD"],
    ["OE"],
    ["OF"],
    ["OH"],
    ["OI"],
    ["OK"],
    ["OM"],
    ["ON"],
    ["OP"],
    ["OR"],
    ["OS"],
    ["OW"],
    ["OX"],
    ["OY"],
    ["PA"],
    ["PE"],
    ["PI"],
    ["PO"],
    ["QI"],
    ["RE"],
    ["SH"],
    ["SI"],
    ["SO"],
    ["TA"],
    ["TE"],
    ["TI"],
    ["TO"],
    ["UH"],
    ["UM"],
    ["UN"],
    ["UP"],
    ["US"],
    ["UT"],
    ["WE"],
    ["WO"],
    ["XI"],
    ["XU"],
    ["YA"],
    ["YE"],
    ["YO"],
    ["ZA"]
]


def twosQuiz():
    # generates 7-letter rack from letters list
    rack = (sorted(random.sample(letters, 7)))
    # test rack w/ 19 valid 2-letter words (no duplicates)
    rack = ['A', 'D', 'E', 'J', 'O', 'T', 'W']
    possibleTwos = []
    validTwos = []
    print('rack: ', rack)

    # generates all 2-letter pairs from rack -- not working (counts each letter as its own pair)
    # not sure if this is even necessary; can validTwos be formed directly from the rack?
    for i in step(0, 6, 1):
        for j in step(0, 6, 1):
            possibleTwos.append([rack[i] + rack[j]])
    print('possible:', possibleTwos)                            # printing for troubleshooting; won't be printed for actual quiz

    # identifies all valid words from all possible 2-letter pairs -- seems to be working
    for m in step(0, len(possibleTwos) - 1, 1):
        for n in step(0, len(twos) - 1, 1):
            if(possibleTwos[m] == twos[n]):
                validTwos.append(twos[n])
    print('valid:', validTwos)                                  # printing for troubleshooting; won't be printed for actual quiz

    # user input
    while True:                                                 # loop continuously
        print("Enter word: ")
        test = []
        inp = input()                                           # get the input
        # need to insert a check against the validTwos...
        # need to insert a break when an incorrect response is entered
        if inp == "":                                           # if it is a blank line...
            break                                               # ...break the loop


twosQuiz()
