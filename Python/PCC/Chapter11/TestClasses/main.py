from classes import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit\n")
while True:
    response = input("Langauges: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\n Thank you for everyone participating in this survey ")
my_survey.show_results()
