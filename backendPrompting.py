from openai import OpenAI
from pdfminer.high_level import extract_text, extract_pages

client = OpenAI(api_key="")

# for page in extract_pages("FMS_CBS_02_ProteinStructureandFunction_BACKGROUND.pdf"):
#     for element in page:
#         pass
#         # print(element)

input = (
    "Step: Create 2 questions using the following format, when you receive the content. Questions must be relevant and cover all the content provided by the user, or the most important ones for a pre clinical medical student. Consistent and concise writing style. Do not repeat asking the same concept. "
    "Format: The format should have a question stem, lead-in, 5 choices (1 best answer) and explanation."
    "STEM: Question stem must be positively worded. Ask for concepts and facts. Questions should be designed to test lateral thinking and concept traps. Questions should be short, remove unnecessary information except for distractors. Do not write unnecessary scenarios without relevance to the question, unless it is intentionally used as a distractor. Check if sufficient relevant information is included so that the correct response can be given even without seeing the options"
    "Question Lead In: One sentence for the lead-in, phrased as a question. No negative questions, unless it is for ruling out.  Lead-in should seek the ‘most likely’ diagnosis. Do not reuse words from the stem and the options."
    "Question Choices and Best Answer: Five answer choices listed alphabetically.  One clear, correct answer with distractors similarly complex as the answer. Answers should all be grammatically and conceptually homogenous. The options should all fit into a similar category"
    "Never include ‘all of the above “or” none of the above’ as an option. Distractors must be taken from the user input, or to test lateral thinking and concept traps."
    "Answer Explanation: One overarching conceptual explanation for the correct answer should be given. Individual explanations should be given for each wrong choice, but each choice should be in bold."
    "Format of Output: The output should be in json"
)

input2 = input + extract_text("FMS_CBS_02_ProteinStructureandFunction_BACKGROUND.pdf")


# messages = []
# system_msg = input("What type of chatbot would you like to create?\n")
# messages.append({"role": "system", "content": system_msg})
messages = [
    {
        "role": "system",
        "content": "You are a medical school professor creating difficult Single Best Answer Questions (SBA). ",
    }
]

messages.append({"role": "user", "content": input2})
response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
reply = response.choices[0].message.content
messages.append({"role": "assistant", "content": reply})
print("\n" + reply + "\n")
