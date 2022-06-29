from question import Question

question_prompts = [
    "What is the capital of India?\n a) Mumbai\n b) Kolkata \n c) New Delhi \n d) Chennai\n\n",
    "What is the national bird of India?\n a) Sparrow\n b) Peacock\n c) Parrot \n d) Mynah\n\n",
    "What is the national animal of India?\n a) Bengal Tiger\n b) Himalayan Lynx\n c) Langoor \n d) Elephant\n\n"
]

question_objects = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a")
]


def run_test(questions):
    score = 0
    for question in question_objects:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1        
    print("You got "+ str(score)+ " out of "+ str(len(question_objects)))

run_test(question_objects)