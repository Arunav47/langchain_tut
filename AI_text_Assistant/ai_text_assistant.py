from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from parser import parser
from prompts import command_promts

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0.2, max_output_tokens=256)

while True:
    user_input = input()
    command, query = parser(user_input)
    if command in command_promts:
        prompt = ChatPromptTemplate.from_template(command_promts[command])
        chain = prompt | model
        output = chain.invoke({"text" : query}).content
        print(output[0]["text"])
    else:
        print("Unknown command")