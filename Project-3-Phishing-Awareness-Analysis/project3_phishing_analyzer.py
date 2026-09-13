import re

message = input("Enter a message to analyze: ")

red_flags = {
    "urgent": "Urgent or threatening language detected",
    "verify your account": "Request to verify an account detected",
    "click here": "Suspicious call-to-action detected",
    "password": "Request for password-related information detected",
    "suspended": "Account suspension threat detected",
    "confirm your identity": "Request for identity confirmation detected"
}

print("\nMessage Analysis:")

message_lower = message.lower()

found_flags = []

for flag in red_flags:
    if flag in message_lower:
        found_flags.append(red_flags[flag])

url_pattern = r"(https?://\S+|www\.\S+)"
suspicious_urls = re.findall(url_pattern, message_lower)

suspicious_url_flags = []

url_shorteners = [
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "is.gd",
    "cutt.ly"
]

suspicious_words = [
    "login",
    "verify",
    "secure",
    "account",
    "password"
]

for url in suspicious_urls:
    if any(shortener in url for shortener in url_shorteners):
        suspicious_url_flags.append(
            f"URL shortener detected: {url}"
        )

    if any(word in url for word in suspicious_words):
        suspicious_url_flags.append(
            f"Suspicious keyword in URL: {url}"
        )

risk_score = len(found_flags) + len(suspicious_url_flags)

print("\nRed flags detected:")

if found_flags:
    for flag in found_flags:
        print("-", flag)
else:
    print("No red flags detected.")

print("\nSuspicious links detected:")

if suspicious_urls:
    for url in suspicious_urls:
        print("-", url)

    if suspicious_url_flags:
        print("\nURL-related red flags:")

        for flag in suspicious_url_flags:
            print("-", flag)
else:
    print("No links detected.")

print("\nRisk Score:", risk_score, "/ 11")

if risk_score >= 6:
    print("Assessment: High Risk - Possible phishing attempt.")
elif risk_score >= 3:
    print("Assessment: Medium Risk - Further investigation recommended.")
else:
    print("Assessment: Low Risk - No major phishing indicators detected.")

print("\nRecommended Action:")

if risk_score >= 6:
    print("- Do not click any links in the message.")
    print("- Do not provide passwords or personal information.")
    print("- Report the message to your IT or security team.")
elif risk_score >= 3:
    print("- Avoid clicking links until the message is verified.")
    print("- Confirm the sender through an official communication channel.")
    print("- Report the message if it appears suspicious.")
else:
    print("- No immediate action required.")
    print("- Continue following normal cybersecurity best practices.")
