import tiktoken

encoder = tiktoken.get_encoding("gpt-3.5-turbo")

print("Vocab size:", encoder.n_vocab)

text = "This is a test sentence. Let's see how it gets tokenized!"
tokens = encoder.encode(text)

print("Tokens: ", tokens)
