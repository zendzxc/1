import prompt
from random import randint


def find_progression():

    name = prompt.string('May I have your name? ')
    print("What number is missing in the progression? ")
    right_answers = 0
    while right_answers != 3:
        num1 = randint(1, 10)
        num2 = randint(80, 100)
        n = randint(2, 10)
        progression = []
        progression = list(range(num1, num2, n))
        index = randint(1, len(progression) - 1)
        correct_answer = progression[index]
        progression[index] = '..'
        new_b = (' '.join(map(str, progression)))

        print(f"Question: {new_b}")
        answer = prompt.string("Your answer: ")
        result = correct_answer

        if int(answer) == result:
            right_answers += 1
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(.Correct answer was '{result}'.
Let's try again, {name}!""")
            right_answers = 0
            return 0
    print(f"Congratulations, {name}!")