from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))  #cliente recebe o valor do construtor

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role":"system",
            "content":"Listar apenas os nomes dos produtos, sem considerar a descrição."
        },
        {
            "role":"user",
            "content":"Liste 3 produtos sustentáveis"
        }
    ],
    model="gpt-4"
)