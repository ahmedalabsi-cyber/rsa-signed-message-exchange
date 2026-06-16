# RSA Signed Message Exchange System

A Python project demonstrating secure message exchange using RSA-2048 digital signatures and SHA-256 hashing.

## Features

- RSA-2048 key generation
- Digital signatures
- SHA-256 hashing
- JSON packet creation
- Signature verification
- Tamper detection

## Project Structure

```text
keygen.py
sign_message.py
verify_message.py
tamper_test.py
requirements.txt
```

## Technologies Used

- Python
- RSA
- SHA-256
- JSON

## Workflow

1. Generate RSA key pairs.
2. Alice signs a message using her private key.
3. Message, signature, and public key are stored in a JSON packet.
4. Receiver verifies the signature.
5. Any message modification causes verification failure.

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python keygen.py
python sign_message.py
python verify_message.py
python tamper_test.py
```

## Learning Outcomes

- Public Key Cryptography
- Digital Signatures
- Hash Functions
- Secure Message Authentication
