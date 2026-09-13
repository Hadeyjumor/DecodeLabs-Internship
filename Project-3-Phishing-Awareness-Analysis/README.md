# Project 3: Phishing Awareness Analysis

## Overview

This project was completed as part of my DecodeLabs cybersecurity internship. It is a beginner-friendly Python lab for analyzing sample emails and messages for common phishing indicators.

The analyzer checks for suspicious keywords, extracts links, identifies selected URL shorteners or suspicious words in URLs, assigns a simple risk score, and provides a recommended action.

## Learning Objectives

- Identify common phishing red flags.
- Recognize suspicious links and social-engineering language.
- Practice basic threat-analysis thinking with Python.
- Understand why suspicious messages require verification before action.

## Features

- Detects common phishing phrases such as urgent requests, account suspension, password requests, and suspicious calls to action.
- Extracts HTTP, HTTPS, and `www` links using regular expressions.
- Flags selected URL-shortening services and suspicious URL keywords.
- Produces a simple risk assessment: Low, Medium, or High.
- Recommends safer next steps based on the assessment.

## Disclaimer

**This project is for lab-test and educational purposes only.** It is a basic awareness exercise and is not a production-grade phishing detector, security product, or substitute for professional security analysis. Its results can be incomplete or inaccurate and should not be treated as proof that a message or URL is safe or malicious. In a professional environment, additional verification would be required, including sender and domain validation, header analysis, reputation checks, sandboxing where appropriate, organizational security controls, and review by qualified security personnel.

Use only authorized sample messages and links for testing. Do not open suspicious links or submit real credentials during testing.

## Requirements

- Python 3.x
- No external libraries required.

## How to Run

```bash
python project3_phishing_analyzer.py
```

Enter a sample message when prompted. The program prints detected red flags, links, risk score, assessment, and recommended action.

## Suggested Test Cases

1. A message containing urgency, account suspension, a password request, and a suspicious link.
2. A legitimate-looking message with no suspicious indicators.
3. A message containing a shortened URL that requires further verification.

## Limitations

- Keyword matching can produce false positives or miss cleverly written phishing messages.
- URL detection does not prove that a link is malicious.
- The risk score is a simple educational heuristic, not a validated security metric.
- Professional analysis requires more context and technical evidence.

## Project Structure

```text
Project-3-Phishing-Awareness-Analysis/
├── project3_phishing_analyzer.py
├── README.md
└── screenshots/
    └── README.md
```

## Skills Practiced

Python, regular expressions, threat identification, phishing awareness, social-engineering analysis, and security thinking.
