import random
import art
import words

print(art.logo)

word = random.choice(words.word_list)
word_list = []
print(word)
for i in range(len(word)):
    word_list.append('_')

lives = 6

finish = False
print(f"{''.join(word_list)}")

while lives > 0 and not finish:

    letter = input("Guess a Letter :")

    if letter in word_list:
        print("You Have already guessed this letter")
        print(art.stages[lives ])
    elif letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                word_list[i] = letter
        print(art.stages[lives ])

    else:
        print("Guessed Letter not in word ")
        lives -= 1
        print(art.stages[lives ])

    if '_' not in word_list:
        print("You Won")
        finish = True

    print(f"{''.join(word_list)}")

if lives == 0:
    print("You Lost")
