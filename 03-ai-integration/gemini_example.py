from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_job_match(cv_summary, job_description):
    prompt = f"""
    Kamu adalah career advisor. Analisis kecocokan kandidat dengan lowongan ini.
    
    CV Kandidat:
    {cv_summary}
    
    Deskripsi Lowongan:
    {job_description}
    
    Berikan:
    1. Skor match (0-100)
    2. Skill yang cocok
    3. Skill yang kurang
    4. Rekomendasi
    
    Jawab dalam Bahasa Indonesia.
    """
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    cv = """
    Backend Developer, 3+ tahun pengalaman.
    Skills: Laravel, PHP, Go, MySQL, PostgreSQL, REST API, Docker, Redis
    Pengalaman: Lead Engineer, ERP development, Agritech platform
    """
    
    job = """
    Dibutuhkan Backend Engineer dengan:
    - Pengalaman Go atau Python minimal 2 tahun
    - Familiar dengan microservices dan Docker
    - Pengalaman dengan PostgreSQL
    - Nice to have: Kubernetes, Redis
    """
    
    print("Menganalisis kecocokan CV dengan lowongan...\n")
    result = analyze_job_match(cv, job)
    print(result)