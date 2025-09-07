import random

WORDS = [
    "sunrise", "planet", "echo", "quantum", "delta", "fusion", "matrix", "shadow",
    "nebula", "crystal", "titanium", "galaxy", "storm", "velocity", "breeze",
    "cosmos", "signal", "flare", "aurora", "nova", "spark", "horizon", "lunar"
]

def generate_password(num_words=4, include_numbers=True, include_symbols=True):
    chosen = random.sample(WORDS, num_words)
    password = "-".join(chosen)

    if include_numbers:
        password += str(random.randint(10, 99))

    if include_symbols:
        password += random.choice("!@#$%^&*?")

    return password

def main():
    print("Password Generator")

    try:
        num_words = int(input("Enter the number of words: "))
    except ValueError:
        print("Enter a valid number.")
        return

    include_numbers = input("Include numbers? (y/n): ").lower() == "y"
    include_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(num_words, include_numbers, include_symbols)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
