import random

# Step 1: Define I/O training data
inputs = [
    "hello",
    "whats your name?",
    "can you code",
    "bye"
]

outputs = [
    "Hi there! What can I help you with? <EOS>",
    "My name is Orion-1 an ai chatbot",
    "No I cant code, but I'm always learning",
    "Bye! See you later. <EOS>"
]

# Step 2: Build bigram dictionary for outputs
bigram_dict = {}
for sentence in outputs:
    words = sentence.split()
    for i in range(len(words) - 1):
        if words[i] not in bigram_dict:
            bigram_dict[words[i]] = []
        bigram_dict[words[i]].append(words[i + 1])

# Step 3: Generate a response given user input
def generate_bigram_response(user_input, max_words=20):
    # Try to match input with closest training input
    matched_index = None
    for i, phrase in enumerate(inputs):
        if phrase in user_input.lower():
            matched_index = i
            break
    
    # Start from first word of corresponding output or random word
    if matched_index is not None:
        sentence = [outputs[matched_index].split()[0]]
    else:
        sentence = [random.choice(list(bigram_dict.keys()))]
    
    # Generate words until <EOS> or max_words
    for _ in range(max_words):
        last_word = sentence[-1]
        next_words = bigram_dict.get(last_word, ["<EOS>"])
        next_word = random.choice(next_words)
        sentence.append(next_word)
        if next_word == "<EOS>":
            break
    return " ".join(sentence).replace("<EOS>", "").strip()

# Step 4: Chat loop
print("AI: Hi! I'm your 2-gram chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("AI:", generate_bigram_response("bye"))
        break
    print("AI:", generate_bigram_response(user_input))