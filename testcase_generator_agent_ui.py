import streamlit as st
import os
from langchain.agents import create_agent
from dotenv import load_dotenv

# Load local .env file if it exists
load_dotenv()

# Bridge Streamlit Cloud Secrets to os.environ if running in the cloud
if "GOOGLE_API_KEY" in st.secrets:
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# Ensure API key is present before running
if not os.environ.get("GOOGLE_API_KEY"):
    st.error("GOOGLE_API_KEY is missing! Please set it in Streamlit Secrets.")
    st.stop()

#i did insatll teh below pacjkages and set the google api key in the .env file
#pip install langchain langchain-google-genai python-dotenv
#model="google_genai:gemini-flash-lite-latest" (or "google_genai:gemini-2.5-flash-lite")


# Custom CSS to increase font size for labels and input boxes
st.markdown("""
    <style>
    /* Increase label font size and color */
    .stTextInput label, .stSelectbox label, .stNumberInput label {
        font-size: 18px !important;
        font-weight: 600 !important;
        color: #2c3e50 !important;
    }
    
    /* Increase input text box font size */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] span, .stNumberInput input {
        font-size: 16px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title(":green[Test Case Generator Agent]")
input_query=st.text_input("Enter your query: ")
test_type=st.selectbox("Enter the test type: ", ["functional", "negative", "positive", "all"])
num_of_testcases=st.number_input("Enter the number of test cases: ", min_value=1, step=1)

System_Prompt="""
You are a test case generator agent. Your task is to generate test cases based 
on the user's input query and specified test type. 
Please provide the requested number of test cases in a clear and structured format as 
below one by one n proper designated test cases format
Testcase ID : \n
Testcses Description:\n
Pre conditions : \n
Steps to reproduce :\n
Testdata: \n
Priority: \n
Expected Result:\n
Status (Pass/Fail): 
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

if st.button(":green[Generate Test Cases]"):
    result=agent.invoke({"messages": [{"role": "user", "content": user_prompt}]})
    st.write(f"Result of response : {result['messages'][-1].text}")