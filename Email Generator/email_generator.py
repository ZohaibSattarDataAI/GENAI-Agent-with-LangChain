from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -----------------------------
# Load LLM
# -----------------------------
model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.3
)

# -----------------------------
# Prompt
# -----------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert business email writer.

Your task is to generate professional emails.

Rules:
- Write a complete email.
- Generate a suitable subject.
- Use professional English.
- Keep formatting clean.
- Be polite.
- Do not explain anything.
- Return only the email.
"""
        ),
        (
            "human",
            """
Email Type:
{email_type}

Purpose:
{purpose}

Receiver:
{receiver}

Sender:
{sender}

Additional Details:
{details}
"""
        )
    ]
)

# -----------------------------
# Parser
# -----------------------------
parser = StrOutputParser()

# -----------------------------
# Runnable Chain
# -----------------------------
chain = prompt | model | parser


# -----------------------------
# Menu
# -----------------------------
def show_menu():
    print("\n" + "=" * 60)
    print("          AI Email Generator")
    print("=" * 60)

    print("1. Leave Application")
    print("2. Internship Request")
    print("3. Job Application")
    print("4. Meeting Request")
    print("5. Project Update")
    print("6. Thank You Email")
    print("7. Complaint Email")
    print("8. Apology Email")
    print("9. Custom Email")
    print("0. Exit")


# -----------------------------
# Main Loop
# -----------------------------
while True:

    show_menu()

    choice = input("\nSelect Option: ")

    if choice == "0":
        print("\nThank you for using AI Email Generator.")
        break

    email_types = {
        "1": "Leave Application",
        "2": "Internship Request",
        "3": "Job Application",
        "4": "Meeting Request",
        "5": "Project Update",
        "6": "Thank You Email",
        "7": "Complaint Email",
        "8": "Apology Email",
        "9": "Custom Email"
    }

    if choice not in email_types:
        print("\nInvalid Option.")
        continue

    print("\nEnter Email Details\n")

    receiver = input("Receiver Name : ")
    sender = input("Your Name     : ")
    purpose = input("Purpose       : ")
    details = input("Extra Details : ")

    response = chain.invoke(
        {
            "email_type": email_types[choice],
            "receiver": receiver,
            "sender": sender,
            "purpose": purpose,
            "details": details
        }
    )

    print("\n" + "=" * 60)
    print("Generated Email")
    print("=" * 60)

    print(response)

    print("=" * 60)