class Developer:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def match_job(self, job):
        match = 0
        for skill in job["required_skills"]:
            if skill in self.skills:
                match += 1
        score = (match / len(job["required_skills"])) * 100
        return round(score, 1)

    def __str__(self):
        return f"{self.name} — Skills: {', '.join(self.skills)}"


class JobBoard:
    def __init__(self):
        self.jobs = []

    def add_job(self, title, required_skills):
        self.jobs.append({"title": title, "required_skills": required_skills})

    def find_best_match(self, developer):
        results = []
        for job in self.jobs:
            score = developer.match_job(job)
            results.append((job["title"], score))
        return sorted(results, key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    # Bikin developer (kamu!)
    fabry = Developer("Fabry", ["Laravel", "Go", "MySQL", "Python", "React"])

    # Bikin job board
    board = JobBoard()
    board.add_job("Backend Developer", ["Laravel", "Go", "MySQL"])
    board.add_job("AI Engineer", ["Python", "PyTorch", "Docker"])
    board.add_job("Fullstack Developer", ["Laravel", "React", "Python"])
    board.add_job("Go Developer", ["Go", "PostgreSQL", "Docker"])

    # Print profil
    print(fabry)
    print("\n=== Job Matches ===")

    # Cari best match
    matches = board.find_best_match(fabry)
    for title, score in matches:
        print(f"{title}: {score}% match")