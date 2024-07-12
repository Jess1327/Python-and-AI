from openai import OpenAI
cilent= OpenAI (api_key="sk-proj-wIkmxYDEHqXboQw92cjwT3BlbkFJNuX2SRG6AHuXirmWqusc")
stop= False
print ("Welcome are you looking for something?")
while stop == False:
    Question=input("what are you looking for?")
    if Question== "stop":
        print("Have good day")
        stop= True
    else:
        data=[
            {"role":"system",
             "content": "You are an assistant that recommends a list of clothing stores based on the question and you figure out the price."},
            {"role":"user","content": Question}
        ]
        response=cilent.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=data
        )
        answer=response.choices[0].message.content
        data.append({"role":"assistant","content":Question})
        print(answer)
