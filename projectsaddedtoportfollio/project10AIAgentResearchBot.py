#importing libraries
from apikey import GEMINI_API_KEY
from google import genai
from google.genai import types
import  wikipedia

#setting up the ai
client = genai.Client(api_key=GEMINI_API_KEY)

#tool that allows the ai to search wikipedia and get the pages
def wikipedia_search(query: str) -> str:
    """Searches Wikipedia for a topic and returns a list of the top 5 matching title pages"""
    try:
       results = wikipedia.search(query, results = 5)
       if not results:
           return f"Sorry! WWe couldn't find results on: '{query}'."
       return f"Search results for '{query}': {', '.join(results)}"
    except Exception as e:
        return f"Error searching Wikipedia: {str(e)}"

#tool that allows ai to get the summary for the wikipedia and choose if it wants to use it
def wikipedia_summary(page_title: str) -> str:
    """Gets an intro summary of a Wikipedia page title"""
    try:
        summary = wikipedia.summary(page_title, sentences = 4, auto_suggest = False)
        return f"Summary of '{page_title}':\n{summary}"
    except wikipedia.DisambiguationError as e:
        return f"'{page_title}' is ambiguous. Did you mean one of these? {', '.join(e.options[:5])}"
    except wikipedia.PageError:
        return f"Page '{page_title}' does not exist. Try searching first."
    except Exception as e:
        return f"Error fetching summary: {str(e)}"


#gives the ai a way to access the tools
tool_map = {
    "wikipedia_search": wikipedia_search,
    "wikipedia_summary": wikipedia_summary
}

#instructions for the ai
SYSTEM_INSTRUCTIONS = """
    You are an autonomous Wikipedia Research Agent. Your goal is to answer the user's request using your tools.
    You operate in a loop: Thought, Action, Observation.
    ...
"""

#function that runs the ai and get research and a response
def run_agent(user_prompt: str, max_iteration: int = 5):
    print(f"Starting research for: '{user_prompt}'\n" + "="*50)
    #making chat
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTIONS,
            tools=[wikipedia_search, wikipedia_summary],
            temperature=0.2
        )
    )
    response = chat.send_message(user_prompt)
    #loop that allows tool use
    for i in range(max_iteration):
        if response.function_calls:
            for call in response.function_calls:
                tool_name = call.name
                tool_args = call.args
                print(f"AI: [Thought/Action] Agent decided to call: {tool_name}({tool_args})")
                tool_function = tool_map[tool_name]
                observation = tool_function(**tool_args)
                response = chat.send_message(
                    types.Part.from_function_response(
                        name=tool_name,
                        response={"result": observation}
                    )
                )
        #end of loop causes success message
        else:
            print(f"\nResearch Complete in {i + 1} steps!\n" + "=" * 50)
            print(response.text)
            return

        #if fail it does this
        print("\nReached maximum iterations without a final answer.")
        print(response.text)

#gets the question and runs the ai
question = input('What would you like my bot to research? ')
run_agent(question)
