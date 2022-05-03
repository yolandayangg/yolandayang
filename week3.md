Create Task Code:
```
name = input("Enter your name:")
print("Welcome, " + name + "!")


def question(question, answer, score):
    print(question)
    while True:
        response = input("Enter an answer: ")

        if response == answer:
            print("Correct")
            score = score + 1
            return score
        if (response != "a") and (response != "b") and (response != "c"):
            print("Please choose from options a, b and c")
        else:
            print("Incorrect.")
            return score


question_bank = [
    "Who is the first president of the United States?\n(a) John F Kennedy\n(b) Abraham Lincoln\n(c) George Washington",
    "When did World War 1 Start\n(a)2022\n(b)1914\n(c)1923",
    "How many people died in the bubonic plague?\n(a)25 million\n(b)40 million\n(c)100 million",
    "Who invented the light bulb?\n(a)Steve Jobs\n(b)Thomas Edison\n(c)Albert Einstein"
]

score = 0

score1 = question(question_bank[0], "c", score),
score2 = question(question_bank[1], "b", score),
score3 = question(question_bank[2], "a", score),
score4 = question(question_bank[3], "b", score)


print("Your result: " + str(score) + "/4")

```


