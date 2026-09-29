from langchain.agents import create_agent
from dotenv import load_dotenv
#i did insatll teh below pacjkages and set the google api key in the .env file
#pip install langchain langchain-google-genai python-dotenv
#model="google_genai:gemini-flash-lite-latest" (or "google_genai:gemini-2.5-flash-lite")

load_dotenv()

input_query=input("Enter your query: ")
test_type=input("Enter the test type: ")
num_of_testcases=input("Enter the number of test cases: ")  

System_Prompt="""
You are a test case generator agent. Your task is to generate test cases based 
on the user's input query and specified test type. 
Please provide the requested number of test cases in a clear and structured format as below
Testcase ID
Pre conditions
Steps to reproduce
Testdata
Priority
Expected Result
Status (Pass/Fail)
IF the test type is functional or positive, use temperature 0
if the test type is negative, use temperature 0.7
if the test type is all, use temperature 0.5
"""

user_prompt=f"""User Requiremnets:
          Query: {input_query}
          Test Type: {test_type}
          number of test cases :{num_of_testcases}
       """
# Create an agent instance using the create_agent function
agent = create_agent(model="google_genai:gemini-flash-lite-latest", system_prompt=System_Prompt)

result=agent.invoke({"messages": [{"role": "user", "content": user_prompt}]})

#print(result["messages"][-1].content)
print(f"Result fo response: {result['messages'][-1].text}")

