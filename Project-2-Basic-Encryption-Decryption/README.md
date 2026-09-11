# Project 2: Basic Encryption & Decryption

## Overview

This project implements a basic Caesar Cipher using Python. The program encrypts user-provided text by shifting alphabetic characters by a selected number and decrypts the encrypted text back to its original form.

## Objective

The objective of this project is to understand basic encryption and decryption concepts, build logical programming skills, and demonstrate how reversible encryption works.

## Features

- Encrypts user-provided text using a Caesar Cipher.
- Decrypts encrypted text using the same shift key.
- Supports uppercase and lowercase letters.
- Preserves spaces, numbers, and special characters.
- Allows the user to select the shift key.

## How It Works

The Caesar Cipher shifts each letter by a specified number of positions in the alphabet.

For example, with a shift key of 3:

```text
A -> D
B -> E
C -> F
```

When the end of the alphabet is reached, the cipher wraps around to the beginning:

```text
X -> A
Y -> B
Z -> C
```

Decryption reverses the process by shifting characters backward using the same key.

## Example

Input:

```text
Hello World
```

Shift key:

```text
3
```

Output:

```text
Original text: Hello World
Encrypted text: Khoor Zruog
Decrypted text: Hello World
```

## Skills Demonstrated

- Python functions
- Loops
- Conditional statements
- String manipulation
- Unicode and ASCII character conversion using `ord()` and `chr()`
- Modulo arithmetic
- Basic encryption concepts
- Data confidentiality fundamentals

## Screenshots

Screenshots of program execution are stored in the `screenshots` folder.

## Disclaimer

This project demonstrates a basic educational encryption technique. A Caesar Cipher is not secure enough for protecting real-world sensitive information.
