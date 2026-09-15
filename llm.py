import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_answer(question: str, context: str):
    prompt = f"""You are a helpful assistant. 
    Answer the question based only on the given context.
    
    Context:
    {context}
    
    Question:
    {question}
    
    Answer:"""

    response = client.chat.completions.create(
        model="groq/compound-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content