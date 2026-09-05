# DecodeLabs Internship — Project 1

## Password Strength Checker 🔐

A Python-based password strength checker developed for DecodeLabs Cyber Security Project 1.

## Features

- Checks password length
- Detects uppercase letters
- Detects lowercase letters
- Detects numbers
- Detects symbols
- Checks against a small list of common passwords
- Detects consecutive repeated characters
- Detects ascending sequential characters
- Calculates a password score
- Classifies passwords as Weak, Medium, or Strong

## Strength Logic

The checker awards points for password length and character variety. Common, repetitive, and sequential passwords are penalized because they are more predictable.

A password is classified as Strong when it is at least 12 characters long, contains uppercase and lowercase letters, numbers and symbols, and is not identified as common, repetitive, or sequential.

## Technologies

- Python 3
- Conditional statements
- Boolean logic
- Lists
- For loops
- String methods

## Security Note

This is an educational password-strength checker. It is not a replacement for professional password auditing tools or a full breached-password database. Password complexity alone does not guarantee security; predictable patterns and commonly used passwords can remain vulnerable to guessing and cracking attacks.

## Project Context

This project was completed as part of the DecodeLabs Cyber Security internship. The implementation goes beyond the core requirements by adding common-password, repetition, and sequential-pattern checks.
