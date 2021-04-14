from Questions import Questions

question_prompts = [
    "What is the color of Donald Duck's bowtie?\n(a) Red\n(b) Yellow\n(c) White\n\n",
    "Lionel Richie was a part of which band?\n(a) King Harvest\n(b) Spectrums\n(c) Commodores\n\n",
    "How old do you have to be to enter the hunger games?\n(a) 11\n(b) 15\n(c) 12\n\n"
    ]

questions = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "c"),
    Questions(question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/"  + str(len(questions)) + " Correct")

run_test(questions)