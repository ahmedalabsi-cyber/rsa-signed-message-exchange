import json
import rsa

# Step 1: Load packet file
with open("json_packet.json", "r") as f:
    packet = json.load(f)

# Step 2: Extract message and signature
message = packet["message"].encode()
signature = bytes.fromhex(packet["signature"])

# Step 3: Load Alice's public key from JSON packet
alice_public_key = rsa.PublicKey.load_pkcs1(
    packet["alice_public_key"].encode()
)

# Step 4: Verify signature
try:
    rsa.verify(message, signature, alice_public_key)
    print("SIGNATURE VALID - Message is authentic and unaltered.")
except rsa.VerificationError:
    print("SIGNATURE INVALID - Message may have been tampered with.")
