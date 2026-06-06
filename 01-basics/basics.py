def main():
    # Contoh dasar Python
    print("Selamat datang di Belajar AI!")
    
    # List comprehension
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    # print(f"Bilangan: {numbers}")
    # print(f"Kuadrat: {squares}")

    skills = ["PHP", "Laravel", "Go", "Python"]
    skill_lengths = [len(s) for s in skills]

    for skill, length in zip(skills, skill_lengths):
        print(f"{skill} punya {length} karakter")
    # Dictionary
    ai_info = {
        "framework": "PyTorch/TensorFlow",
        "language": "Python",
        "level": "Beginner"
    }
    # print(f"Info AI: {ai_info['framework']}")

    # Simulasi sederhana "AI scoring" seperti yang kita lakukan tadi
    def score_job(job, my_skills):
        match = 0
        for skill in job["required_skills"]:
            if skill in my_skills:
                match += 1
        score = (match / len(job["required_skills"])) * 100
        return round(score, 1)

    jobs = [
        {"title": "Backend Developer", "required_skills": ["Laravel", "Go", "MySQL"]},
        {"title": "AI Engineer", "required_skills": ["Python", "PyTorch", "Docker"]},
        {"title": "Fullstack Developer", "required_skills": ["Laravel", "React", "Python"]},
    ]

    my_skills = ["Laravel", "Go", "MySQL", "Python", "React"]

    for job in jobs:
        score = score_job(job, my_skills)  # ← pastikan ada 2 argumen di sini
        print(f"{job['title']}: {score}% match")

if __name__ == "__main__":
    main()
