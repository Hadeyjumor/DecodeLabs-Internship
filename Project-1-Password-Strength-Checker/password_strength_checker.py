password = input("Enter a password: ")

# List of common passwords to check against
common_passwords = [
    "password",
    "12345678",
    "123456789",
    "qwerty",
    "password1",
    "admin",
    "welcome"
]

# Flags to track password characteristics
has_uppercase = False
has_lowercase = False
has_number = False
has_symbol = False
has_repetition = False
has_sequence = False
is_common = False
is_strong = False

# Check character types
for char in password:
    if char.isupper():
        has_uppercase = True

    if char.islower():
        has_lowercase = True

    if char.isdigit():
        has_number = True

    if not char.isalnum():
        has_symbol = True

# Check for common passwords
if password.lower() in common_passwords:
    is_common = True

# Check for consecutive repeated characters
for i in range(len(password) - 1):
    if password[i] == password[i + 1]:
        has_repetition = True

# Check for ascending sequential characters
for i in range(len(password) - 3):
    if (
        ord(password[i + 1]) == ord(password[i]) + 1
        and ord(password[i + 2]) == ord(password[i + 1]) + 1
        and ord(password[i + 3]) == ord(password[i + 2]) + 1
    ):
        has_sequence = True

# Display password analysis
print("\n--- Password Analysis ---")
print("Password length:", len(password))
print("Has uppercase letter:", has_uppercase)
print("Has lowercase letter:", has_lowercase)
print("Has number:", has_number)
print("Has symbol:", has_symbol)
print("Has repeated characters:", has_repetition)
print("Has sequential characters:", has_sequence)
print("Is a common password:", is_common)

# Calculate password score
score = 0

if len(password) >= 8:
    score += 1

if len(password) >= 12:
    score += 1

if has_uppercase:
    score += 1

if has_lowercase:
    score += 1

if has_number:
    score += 1

if has_symbol:
    score += 1

# Common, repetitive, or sequential passwords lose strength
if is_common:
    score = 0
elif has_repetition or has_sequence:
    score = max(0, score - 2)

# Determine whether password is strong
if (
    len(password) >= 12
    and has_uppercase
    and has_lowercase
    and has_number
    and has_symbol
    and not is_common
    and not has_repetition
    and not has_sequence
):
    is_strong = True

print("Password score:", score)

# Determine final password strength
if is_strong:
    print("Password strength: STRONG")
elif score >= 3:
    print("Password strength: MEDIUM")
else:
    print("Password strength: WEAK")
