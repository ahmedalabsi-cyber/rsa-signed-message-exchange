import rsa

def rsakeygeneration(name,key_size=2048):
    
    print(f"generate RSA key pair for : {name.upper()}")
    
    
    #generate key pair for alice 
    
    alice_public_key , alice_private_key = rsa.newkeys(key_size) 
    
    
    #save public key for alice
    alice_public_key_path='alice_public_key.pem'
    with open(alice_public_key_path, 'wb') as f:
        f.write(alice_public_key.save_pkcs1())
        print(f"Alices's public key is save in :- {alice_public_key_path}")
        
    #save private key alice 
    alice_private_key_path='alice_private_key.pem'
    with open(alice_private_key_path, 'wb') as f:
        f.write(alice_private_key.save_pkcs1())
        print(f"Alice's private key is save in :- {alice_private_key_path}")
     
    print("alice's keys are saved now ")   
        
   
    #generate key pair for bob 
    
    bob_public_key , bob_private_key = rsa.newkeys(key_size)
    
    #save public key for bob
    bob_public_key_path='bob_public_key.pem'
    with open(bob_public_key_path, 'wb') as f:
        f.write(bob_public_key.save_pkcs1())
        print(f"Bob's public key is saved in :- {bob_public_key_path}")
        
    #save private key bob 
    bob_private_key_path='bob_private_key.pem'
    with open(bob_private_key_path, 'wb') as f:
        f.write(bob_private_key.save_pkcs1())
        print(f"Bob's private key is save in :- {bob_private_key_path}")
        
    
    print("bob's key is saved now ") 
    
    
    # information about the keys
    print(" alices key :-")
    print(alice_public_key.save_pkcs1().decode())
    
    
    print(" bob's key :-")
    print(bob_public_key.save_pkcs1().decode())
    
    
    print(f'they key size that has been used is :{key_size}')
    
    
    print("now there's four files that has beeen created ")

    
rsakeygeneration("alice and bob")
    
print("-----------------------------")
print("Done! 4 files created:")
print("  - alice_public_key.pem")
print("  - alice_private_key.pem")
print("  - bob_public_key.pem")
print("  - bob_private_key.pem")
print("-----------------------------")
    
    
