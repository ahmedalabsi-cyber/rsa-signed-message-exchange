import rsa 
import hashlib
import json




def aliceSender():
    with open("alice_private_key.pem","rb") as f :
        alice_private_key=rsa.PrivateKey.load_pkcs1(f.read())
        print("Alice's private key has been loaded successfuly  ")
        
    message=" Hello bob, this is me alice i wanted to share with you this secret information. [20230002922,20230003483,20230003072,20230003830]"
    
    
    hash_of_message=hashlib.sha256(message.encode()).hexdigest()
    
    print(f" your SHA-256 message hash is :- {hash_of_message} ")
    
    
    # we sign the hash 
    signature=rsa.sign(message.encode(),alice_private_key, "SHA-256") #encode() --> convert text to bytes 
                                                                      # "sha-256" --> the the hashing algorthim we used 
    
    #load alice public key, so we can put it in packet so bob can verify later  
    with open("alice_public_key.pem" , "rb") as f:
        alice_public_key=rsa.PublicKey.load_pkcs1(f.read())   #load_pkcs1()--->Read key that was saved in PKCS1 format
        print("Alice's public key has been loaded successfuly  ")
        
    
    # now we gonna save everything in json packet 
    
    json_packet= {
        "message" :message,
        "signature" : signature.hex(),
        "alice_public_key" :alice_public_key.save_pkcs1().decode() #decode()  ---> covert the bytes to text 
                                                                   #save_pkcs1() ---> Save key in PKCS1 format
    }    
    
    
    with open("json_packet.json" , "w") as f :
        json.dump(json_packet,f ,indent=4)     #json_packet ---> is all your items (message, signature, public key)
                                               #.dump() --------> convert and write into a file
                                               #f        -------> the file we opened (json_packet.json)
                                               # indent=4  ------> we gonna add 4 spaces so the information looks organaized in the "json_packet.json"

        
        
    print ("the packet is now saved in 'json_packet.json' ")
    
aliceSender() #we called the function so we can run the code 
    
    
        
    
    
    
    
