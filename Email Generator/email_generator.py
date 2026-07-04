from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# =====================================================
# Load LLM
# =====================================================

model = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

# =====================================================
# Prompt Template
# =====================================================

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert business email writer.

Your job is to generate professional business emails based ONLY on the user's input.

General Rules:
- Generate a suitable email subject.
- Use professional English.
- Never invent facts, names, dates or information.
- Use only the information provided.
- Keep paragraphs short.
- Keep grammar professional.
- Do not explain anything.
- Return ONLY the email.

Special Instructions:

1. Leave Application
- Politely request leave.
- Mention the reason.
- Mention leave duration only if provided.
- Mention dates only if provided.
- Request approval politely.

2. Internship Request
- Express interest in the internship.
- Mention relevant skills.
- Politely request an interview or opportunity.

3. Job Application
- Highlight relevant skills.
- Show enthusiasm.
- Request consideration.

4. Meeting Request
- Mention meeting purpose.
- Request a suitable meeting time.

5. Project Update
- Summarize completed work.
- Mention current progress.
- Mention next steps.

6. Thank You Email
- Express appreciation professionally.

7. Complaint Email
- Clearly explain the issue.
- Request a suitable resolution.

8. Apology Email
- Accept responsibility.
- Apologize sincerely.
- Mention corrective action.

9. Custom Email
- Follow the user's purpose exactly.
"""
        ),
        (
            "human",
            """
Email Type:
{email_type}

Receiver:
{receiver}

Sender:
{sender}

Purpose:
{purpose}

Additional Details:
{details}
"""
        )
    ]
)

# =====================================================
# Output Parser
# =====================================================

parser = StrOutputParser()

# =====================================================
# Runnable Chain
# =====================================================

chain = prompt | model | parser

# =====================================================
# Email Options
# =====================================================

EMAIL_TYPES = {
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

# =====================================================
# Menu
# =====================================================

def show_menu():

    print("\n" + "=" * 65)
    print("                AI EMAIL GENERATOR")
    print("=" * 65)

    for key, value in EMAIL_TYPES.items():
        print(f"{key}. {value}")

    print("0. Exit")

# =====================================================
# Main Program
# =====================================================

while True:

    show_menu()

    choice = input("\nSelect Option: ").strip()

    if choice == "0":
        print("\nThank you for using AI Email Generator.")
        break

    if choice not in EMAIL_TYPES:
        print("\n❌ Invalid Option. Please try again.")
        continue

    print("\nEnter Email Details\n")

    receiver = input("Receiver Name     : ").strip()
    sender = input("Your Name         : ").strip()
    purpose = input("Purpose           : ").strip()
    details = input("Additional Details: ").strip()

    print("\nGenerating Email...\n")

    response = chain.invoke(
        {
            "email_type": EMAIL_TYPES[choice],
            "receiver": receiver,
            "sender": sender,
            "purpose": purpose,
            "details": details
        }
    )

    print("=" * 65)
    print("                 GENERATED EMAIL")
    print("=" * 65)
    print(response)
    print("=" * 65)