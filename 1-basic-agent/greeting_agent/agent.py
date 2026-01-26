from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm 

root_agent = Agent(
    name="greeting_agent",
    # Update the model string here
    # model = 'gemini-2.0-flash',
    model=LiteLlm(model="gpt-4.1-nano"),
    
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    """,
)