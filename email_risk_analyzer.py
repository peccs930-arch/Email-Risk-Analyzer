import re

print("=" * 50)
print("        EMAIL RISK ANALYZER")
print("=" * 50)

filename = input("Enter email text file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        email = file.read()

    score = 0

    suspicious_words = [
        "urgent",
        "verify",
        "password",
        "bank",
        "account",
        "click",
        "login",
        "winner",
        "lottery",
        "gift",
        "prize",
        "free",
        "limited offer"
    ]

    print("\nChecking email...\n")

    for word in suspicious_words:
        if word.lower() in email.lower():
            print(f"Found suspicious keyword: {word}")
            score += 1

    urls = re.findall(r'https?://\S+', email)

    if urls:
        print("\nLinks Found:")
        for url in urls:
            print(url)
        score += len(urls)

    if score <= 2:
        risk = "LOW"
    elif score <= 5:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    print("\n" + "="*40)
    print("EMAIL RISK REPORT")
    print("="*40)
    print(f"Risk Score : {score}")
    print(f"Risk Level : {risk}")

except FileNotFoundError:
    print("Email file not found.")
