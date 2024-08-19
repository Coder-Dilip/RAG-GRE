from django.shortcuts import render
import os
from groq import Groq
import random
import re
# Create your views here.
def index(req):
    client = Groq(
        api_key='',
    )
    
    # Vocabulary groups
    vocab_groups = [
        {
            "group_name": "Anger",
            "words": ["enrage", "fume", "infuriating", "ire", "irate"]
        },
        {
            "group_name": "Inclination",
            "words": ["predilection", "disposed", "affinity", "predisposition", "proclivity", "propensity", "aptitude"]
        },
        {
            "group_name":"Prediction",
            "words":["Augur","Prognosis","Presage", "Prescience","Anticipates", "Forecast","Foresight","Foretell","Foresee"]
        }
        # Add more vocabulary groups here
    ]

        # Select a random vocabulary group for group1
    group1 = random.choice(vocab_groups)

    # Ensure group2 is not the same as group1
    while True:

        group2 = random.choice(vocab_groups)

        if group2 != group1:
            break
        
    while True:
        group3 = random.choice(vocab_groups)

        if group3 != group1 and group3!= group2:
            break

    # Select a random word from group1 and group2
    word1 = random.choice(group1["words"])
    word2 = random.choice(group2["words"])
    word3=random.choice(group3['words'])
    print("hello",word1,word2,word3)
    example_response=[
        {
  "question": "The detective's _____ investigation led to a _____ breakthrough in the case.",
  "blank1_options": ["meticulous", "sloppy", "superficial", "cursory"],
  "blank2_options": ["unexpected", "anticipated", "minor", "predictable"],
  "correct_answer": ["meticulous", "unexpected"],
  "explanation": '''The correct answer is meticulous and unexpected. A meticulous investigation is thorough and detailed, which would likely lead to an unexpected breakthrough. The contrast between the detective's careful work and the surprising outcome creates a strong connection. The other options do not fit the context as well.'''
},

{
  "question": "The detective's _____ investigation led to a major breakthrough in the case.",
  
  "blank1_options": ["meticulous", "sloppy", "superficial", "cursory"],
  
  "correct_answer": ["meticulous"],
  
  "explanation": '''The correct answer is meticulous. A meticulous investigation is thorough and detailed, which increases the likelihood of discovering significant breakthroughs. The other options do not suggest the same level of careful attention and thoroughness.'''
},

{
  "question": "The detective's _____ investigation, coupled with the _____ evidence, led to a _____ breakthrough in the case.",
  
  "blank1_options": ["meticulous", "sloppy", "superficial", "cursory"],
  
  "blank2_options": ["vital", "irrelevant", "minimal", "routine"],
  
  "blank3_options": ["surprising", "predictable", "minor", "insignificant"],
  
  "correct_answer": ["meticulous", "vital", "surprising"],
  
  "explanation": '''The correct answers are meticulous, vital, and surprising. A meticulous investigation is thorough and detailed, and vital evidence is crucial for solving the case. These factors combined can lead to a surprising breakthrough, adding an element of unexpected discovery to the resolution of the case. The other options do not create the same impactful scenario.'''
}
]

    message=[
            {
                "role": "user",
                "content": f'''Create a GRE-style question in json format using the following words as correct options or answers: '{word1}, {word2}'. for each blank there should be only one correct answer. Don't put synonym of correct answer in same option list."
        "Number of blanks should be two"
        "Provide multiple-choice options for the blank. make sure there will be only one correct answer. correct option should not be having any synonym in the option list"
        "Finally, provide the correct answer to the blank",
        "Response should be in json format. look at this example response: {example_response[0]}"''',
        
            },

             {
                "role": "user",
                "content": f'''Create a GRE-style question in json format using the following word as correct option or answer: '{word1}'. For the blank there should be only one correct answer. Don't put synonym of correct answer in same option list."
        "Number of blanks should be only one"
        "Provide multiple-choice options for the blank. make sure there will be only one correct answer. correct option should not be having any synonym in the option list"
        "Finally, provide the correct answer to the blank",
        "Response should be in json format. look at this example response: {example_response[1]}"''',
        
            },

            {
                "role": "user",
                "content": f'''Create a GRE-style question in json format using the following words as correct options or answers: '{word1}, {word2}, {word3}'. for each blank there should be only one correct answer. Don't put synonym of correct answer in same option list."
        "Number of blanks should be three"
        "Provide multiple-choice options for the blank. make sure there will be only one correct answer. correct option should not be having any synonym in the option list"
        "Finally, provide the correct answer to the blank",
        "Response should be in json format. look at this example response: {example_response[2]}"''',
        
            },

        ]
   
    chat_completion = client.chat.completions.create(
        messages=[random.choice(message)],
        model="llama-3.1-70b-versatile",
    )

    response=chat_completion.choices[0].message.content
    # Use regex to find JSON part
    match = re.search(r'\{[^}]+\}', response, re.DOTALL)
    json_string=''
    # Check if a match was found
    if match:
        json_string = match.group(0)
    else:
        print("No JSON found.")
    
    print(json_string)
    return render(req,'index.html',{'data':json_string})