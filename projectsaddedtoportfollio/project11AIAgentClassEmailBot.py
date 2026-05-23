from projectsaddedtoportfollio.apikey import GEMINI_API_KEY
from google import genai
from google.genai import types
import smtplib
import ssl
from email.message import EmailMessage
from langchain_core.tools import tool
from email_info import email_address, app_passwordc

CLASS_SCHEDULE = {
    "RSM-Algebra": [
        {"day": "monday",
        "time": "5:45 PM",
         }
        ],
    "RSM-Geo": [
        {"day": "friday",
         "time": "5:15 PM"
         }
        ],
    "Badminton-TeamCGold1": [
        {"day": "saturday",
         "time": "2:00 PM"
         }
    ],
    "Badminton-TeamCGold2": [
        {"day": "sunday",
         "time": "4:15 PM"
         }
    ]
}

@tool
def check_class_schedule(day_of_week: str) -> str:
    """Look up what classes are scheduled for a specific day of the week (e.g., 'Monday', 'Friday')."""
    target_day = day_of_week.lower() #looks for today and puts it into a variable
    found_classes = [] #made a list for the classes that are found
    for class_name, schedule_list in CLASS_SCHEDULE.items(): #makes class name the name of the class and schedule list the list of data in the class name
        for schedule in schedule_list: #examines the data inside the list
            if schedule["day"] == target_day: #if the day in the schedule is the same as today it adds it to the found classes
                found_classes.append({"name": class_name, "time": schedule["time"]}) #adds to the found classes

    if not found_classes: #returns nothing found if nothing fits
        return f"No classes schedules for {day_of_week}"

    result = f"Classes for {day_of_week.capitalize()}:\n" #says that there are classes today if there are
    for class_found in found_classes: #for each class that day returns the name and time of the class from the found_classes list
        result += f"- {class_found['name']} at {class_found['time']}\n"
    return result

@tool
def send_email_reminder(email_body: str, recipient_emails: str = email_address) -> str :
    """Sends an email notification to the user with their class details."""
    #making email details
    sender_email = email_address
    app_pass = app_password
    msg = EmailMessage()
    msg['Subject'] = "Class Reminder"
    msg['From'] = sender_email
    msg['To'] = recipient_emails
    msg.set_content(email_body)
    context = ssl.create_default_context()
    #making the sending logic
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: #sets up secure connection
            #logs in and sends email
            smtp.login(sender_email, app_pass)
            smtp.send_message(msg)
            return "Email sent successfully"
    #says couldn't return if there was an error
    except Exception as e:
        return f"Failed to send email. Error: {e}"

client = genai.Client(api_key = GEMINI_API_KEY)
tool_list = [check_class_schedule, send_email_reminder]
tools_map = {tool.name: tool for tool in tool_list}


def run_agent(user_prompt: str):
    chat = client.chats.create(
        model='gemini-2.5-flash',
        config=types.GenerateContentConfig(
            tools = [t.func for t in tool_list],
            system_instruction=(
                "You are a dedicated class schedule scheduling assistant. You have absolute "
                "permission and access to look up information using 'check_class_schedule' and "
                "transmit notifications using 'send_email_reminder'. Never tell the user you "
                "lack real-world access or capabilities; always execute your tools when asked."
            )
        )  # <-- Parentheses closed here now!
    )
    response = chat.send_message(user_prompt)


    while response.function_calls:
        for function_call in response.function_calls:
            name = function_call.name
            arguments = function_call.args

            # Get the real Python function and execute it locally
            tool_to_call = tools_map[name]
            tool_result = tool_to_call.invoke(arguments)

            print(f"[Tool Run] {name} output: {tool_result}")


            response = chat.send_message(
                message=f"Tool '{name}' completed. Result: {tool_result}"
            )


    print(f"\nAgent: {response.text}")

prompt = input('What do you want to check today? ')
run_agent(prompt)