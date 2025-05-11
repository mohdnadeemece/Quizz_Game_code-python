import json

def load_questions(question):
    with open(question,"r") as file:
        return json.load(file)
    

def run_quiz(question):
    score=0

    for idx, q in enumerate(question):
        print(f"\nQ{idx+1}:{q['question']}")

        for i, option in enumerate(q['options']):
            print(f"{i+1}. {option}")

        answer = int(input("Enter your answer option (1-4): "))

        if q['options'][answer-1]==q['answer']:
                print("✅ Correct!")
                score+=1

        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")    

    print(f"\n Your final score is: {score}")            

if __name__=="__main__":
    question=load_questions("question")
    run_quiz(question)
