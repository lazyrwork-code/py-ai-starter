from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# "Database" lowongan kita
JOBS = [
    "Posisi: Senior Backend Developer | Perusahaan: TechStartup Jakarta | Requirements: Laravel 5+ tahun, MySQL, REST API, Docker | Gaji: 20-30 juta | Remote: Yes",
    "Posisi: Go Engineer | Perusahaan: Fintech Bandung | Requirements: Go 2+ tahun, PostgreSQL, Docker, microservices | Gaji: 25-35 juta | Remote: Hybrid",
    "Posisi: AI Engineer | Perusahaan: AI Startup Surabaya | Requirements: Python 3+ tahun, PyTorch, Docker | Gaji: 30-45 juta | Remote: Yes",
    "Posisi: Fullstack Developer | Perusahaan: Software House Malang | Requirements: Laravel, Vue.js, MySQL | Gaji: 10-18 juta | Remote: No",
]

CV = """
Fabryzal Adam Pramudya - Backend Developer, 3+ tahun.
Skills: Laravel, PHP, Go, MySQL, PostgreSQL, REST API, Docker, Redis, Vue.js, React.js
Pengalaman: Lead Engineer, ERP development, Agritech platform
"""

def rag_query(question):
    # Gabungkan semua dokumen sebagai konteks
    context = "\n\n".join([f"Lowongan {i+1}:\n{job}" for i, job in enumerate(JOBS)])
    
    prompt = f"""
    Kamu adalah career advisor. Jawab pertanyaan berdasarkan data lowongan berikut saja.
    
    DATA LOWONGAN:
    {context}
    
    CV KANDIDAT:
    {CV}
    
    PERTANYAAN: {question}
    
    Jawab dalam Bahasa Indonesia berdasarkan data di atas.
    """
    
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    questions = [
        "Mana lowongan yang paling cocok dengan CV saya? Jelaskan alasannya.",
        "Lowongan mana yang remote dan gaji tertinggi?",
        "Skill apa yang perlu saya tambah untuk lolos semua lowongan?"
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"=== Pertanyaan {i} ===")
        print(f"Q: {question}")
        print(f"A: {rag_query(question)}\n")