##total_bill_amount = float(input("Total bill: "))
##tip = float(input("Tip: "))

##tip_amount = total_bill_amount*(tip/100)

##final_bill = total_bill_amount + tip_amount

##print(f"Total bill: {final_bill:.2f}")

Questions_And_Answers = {
    "What is the capital of Australia?" : "Canberra",
    "What is the chemical symbol for gold?" : "Au",
    "In computing, what does CPU stand for?" : "Central Processing Unit"
}
score = 0
questions = 0
for question, answer in Questions_And_Answers.items():

    your_answer = input(f"Question: {question} \n type your answer:")
    questions += 1
    if your_answer == answer:
        print(f"Correct! your answer {your_answer} to {question} is correct.")
        score += 1
    else:
        print(f"Incorrect! your answer {your_answer} to {question} is incorrect. the correct answer is {answer}.")

print(f"Your score is {score}/{questions}.")

