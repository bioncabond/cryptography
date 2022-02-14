import nltk 
# nltk.download_shell()  

words_list= nltk.corpus.words.words()

def encrypt(msg,key): 
    encrypted_msg = "" 
    msg = msg.lower()
    key = key % 26  

    for char in str(msg): 
        if ord(char) not in range(97,123): 
            encrypted_msg += char 

        else: 
        #     #this gets us the ascii code and the key 
            add_char = (ord(char) + key) 
            # print(f"this is add letter: {add_letter}")
            # if the letter is outside of our range we want to handle
            #how to restart the letter loop 
            if add_char > 122: 
                #how far are we from the end of the alphabet  
                letters_end = 122 - ord(char) 
                # print(f"this is ord(char)/ascii: {ord(char)}")

                move_over = key - letters_end - 1 
                # print(f"move_over: key {key}, letters_end: {letters_end}")

                letter_a_start = 97 + move_over  
                # print(f"this is letter_a_start: {letter_a_start} ") 

                encrypted_msg += chr(letter_a_start)
            else:
                encrypted_msg += chr(ord(char)+ key)
    # print(f"encrypted message final: {encrypted_msg}")

    return encrypted_msg

def decrypt(msg,key): 
    return encrypt(msg,-key) 

def real_words(msg): 
    num_of_words = 0
    words = msg.split(" ")
   
    for word in words:
        if word in words_list:
            num_of_words += 1
    if (num_of_words/len(words)) >= 0.5:
        # print(f"num_of_words: {num_of_words}") 
        return num_of_words 
    else:
        return 0

def crack(msg): 
    max = 0
    msg = msg.lower() 
    sentence = ""
    for key in range(26): 
        decrypt_msg = decrypt(msg, key) 
        num_of_words = real_words(decrypt_msg) 

        if num_of_words > max:
            sentence = decrypt_msg 
            print(f"crack num_of_words: {num_of_words}") 
            print(f"crack sentence: {sentence}")
    return sentence

if __name__== "__main__": 
    words_list = nltk.corpus.words.words() 

    # msg = encrypt("hell0 w0rld$",3)
    # msg = encrypt("It was the best of times, it was the worst of times.",3)
    # print(f"encrypt: {msg}") 
    # real_words_msg = real_words("hello world blue") 
    # crack_msg = crack("hello world crack")
   