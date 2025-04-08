import tokzilla as ty

encoder_decoder = ty.Encoder(vocab_size=100)

text = "This is a test program to run tokzilla"

encoded = encoder_decoder.encode(text)
print(f"Encoded: {encoded}")

decoded = encoder_decoder.decode(encoded)
print(f"Decoded: {decoded}")