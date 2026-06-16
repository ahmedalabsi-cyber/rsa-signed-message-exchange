import json
import rsa
import hashlib

# load packet we saved earlier
with open("json_packet.json", "r") as file:
    packetData = json.load(file)

msg = packetData["message"]
sig_hex = packetData["signature"]

sig_bytes = bytes.fromhex(sig_hex)

public_key_raw = packetData["alice_public_key"]
publicKey = public_key_raw.encode()

aliceKey = rsa.PublicKey.load_pkcs1(publicKey)

print("Original message:")
print(msg)


# recompute hash to check integrity
hash_obj = hashlib.sha256(msg.encode())
hash_value = hash_obj.hexdigest()
print("\nRecomputed SHA-256 hash:")
print(hash_value)


# check if the signature matches the message from alice
print("\nVerifying original message")

try:
    #Keeping arguments split for readability
    rsa.verify(
        msg.encode(),
        sig_bytes,
        aliceKey
    )

    print("SIGNATURE VALID - Message is authentic and unaltered.")

except Exception as error:
    #Printing error might help debugging later
    print(error)
    print("SIGNATURE INVALID")


print("\nTampering the original message")

#Change "Hello" to "Hallo" in the message
tamperedMsg = msg.replace("Hello", "Hallo")

print("\nTampered message:")
print(tamperedMsg)


#Recompute hash again after tampering
hash_val_obj = hashlib.sha256(tamperedMsg.encode())
hash_value = hash_val_obj.hexdigest()

print("\nRecomputed SHA-256 hash after tampering:")
print(hash_value)


print("\nVerifying tampered message")

try:
    rsa.verify(
        tamperedMsg.encode(),
        sig_bytes,
        aliceKey
    )

    print("SIGNATURE VALID")

except Exception as error:
    print(error)
    print("SIGNATURE INVALID - Message may have been tampered with.")
