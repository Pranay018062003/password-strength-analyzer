import re

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@$!%*?&]", password):
        score += 1
    return score

pwd = input("Enter password to check strength: ")
strength = check_strength(pwd)

print(f"Password Strength Score: {strength}/5")
