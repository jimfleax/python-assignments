def analyze_password(password):
    if len(password) < 8:
        return "🔴 WEAK (Must be at least 8 characters)"

    has_upper = False
    has_number = False
    has_symbol = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.isdigit():
            has_number = True
        elif not char.isalnum():
            has_symbol = True

    score = has_upper + has_number + has_symbol

    if score == 3:
        return "STRONG (Excellent variety)"
    elif score == 2:
        return "MEDIUM (Good, but missing a number or symbol)"
    else:
        return "WEAK (Needs uppercase, numbers, and symbols)"


print("=== SECURE PASSWORD ANALYZER ===")
print("Type 'exit' anytime to quit.\n")

while True:
    user_input = input("Enter a password to test: ")

    if user_input.lower() == "exit":
        print("System shutting down...")
        break

    if user_input == "":
        print("Please enter a valid password.")
        continue

    result = analyze_password(user_input)

    print(f"Result: {result}")
    print("-" * 30)
