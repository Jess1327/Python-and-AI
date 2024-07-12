from openai import OpenAI

Welcome_Message = input("Welcome, are you ready to take the style quiz?")
Paragraph = ""
if Welcome_Message == "yes":
    print("Okay lets get STARTED")
    Question1 = input("What mainly consite in your closet?")
    Question2 = input(" Do you know what your style is?")
    Question3 = input(" What is mostly in your closet?")
    Question4 = input("What is your favoirte seaoson?")
    Question5 = input("Favorite color")
    Question6 = input("What is your favorite Accesseories")
    Paragraph = "This persons closet is consites of: " + Question1 +".This users style is: " + Question2 +".This User mostly has in their closet: " + Question3 + ".This users favortite season is: " + Question4 +".This User favortite color is: " + Question5 +".This users favortite accessories is: " + Question6

cilent = OpenAI(api_key="sk-proj-wIkmxYDEHqXboQw92cjwT3BlbkFJNuX2SRG6AHuXirmWqusc")
stop = False
# while stop == False:
# # if Question== "stop":
#     print("Have good day")
#     stop= True
# else:
data = [
    {"role": "system",
     "content" : "based on this user input give one aesthetic and list the top 7 clothing stores for them to shop at and the budget and why you recommend it the product"},
     # "content": "You should figure out the users aesthtic then the list of stores ordered by budjet and then explain why you recommend it"},
    {"role": "user", "content": Paragraph}
]
response = cilent.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=data
)
answer = response.choices[0].message.content
data.append({"role": "assistant", "content": answer})
print(answer)
