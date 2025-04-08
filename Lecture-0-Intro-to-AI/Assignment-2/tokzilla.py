class Encoder:
    def __init__(self, vocab_size=10000):
        self.vocab_size = vocab_size
        
    def encode(self, text):
        tokens = text.split() #-> splits the string after each space
        encoded_tokens = [] #--> empty array to store the tokens of the string
        for token in tokens:
            ascii_str = "".join(str(ord(char)) for char in token) #--> ord(char) --> returns the unicode of the particular character which is then converted into string by 'str' which is then joined using the .join function in the empty string of ascii_str. This is done for every character present in the particular word using the for char in token loop
            encoded_token = int(ascii_str) #--> convert the str to int 
            encoded_tokens.append(encoded_token) #--> append the converted str into the array
        return encoded_tokens

    def decode(self, encoded_tokens):
        decoded_tokens = []
        for number in encoded_tokens:
            digits = str(number) #--> converts the number of the token into a string
            i = 0
            token = ""
            while i < len(digits):
                if i + 3 <= len(digits) and 32 <= int(digits[i : i + 3]) <= 126: #--> checks for 3 digit ascii values, first condition checks if i+3 is not out of bounds the second condition checks if the integer present at the position from i to i+3(in this case 0 to 2; 3 not included), is between 32 ans 126 (ascii value range)
                    token += chr(int(digits[i : i + 3])) #--> if the condition satisfies it converts the digit into an int and then converts it into the actual character and adds it to the token string
                    i += 3
                elif i + 2 <= len(digits) and 32 <= int(digits[i : i + 2]) <= 126: #--> same for 2 digits
                    token += chr(int(digits[i : i + 2]))
                    i += 2
                else:
                    token += "?" #--> checks for unnecessary charsif present
                    break
            decoded_tokens.append(token) #--> append the token into the decoded tokens array
        return " ".join(decoded_tokens)#--> join the decodedtoken with a space between each word


def main():
    encoder = Encoder()
    text = "Hello there! How have you been?"
    encoded = encoder.encode(text)
    print(f"Encoded: {encoded}")
    decoded = encoder.decode(encoded)
    print(f"Decoded: {decoded}")


if __name__ == "__main__":#--> when we import the file we only need the encoder and decoder function and not the main  method, so when we import it this condition becomes false and the main() doesn't run while in this file the main function exists making the condition true
    main()