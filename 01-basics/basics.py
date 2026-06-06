def main():
    # Contoh dasar Python
    print("Selamat datang di Belajar AI!")
    
    # List comprehension
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print(f"Bilangan: {numbers}")
    print(f"Kuadrat: {squares}")

    # Dictionary
    ai_info = {
        "framework": "PyTorch/TensorFlow",
        "language": "Python",
        "level": "Beginner"
    }
    print(f"Info AI: {ai_info['framework']}")

if __name__ == "__main__":
    main()
