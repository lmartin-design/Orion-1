import random

inputs = [
    "Hello",
    "Whats your name?",
    "Can you code",
    "exit"
]

outputs = [
    "Hi there! What can I help you with? <EOS>",
    "My name is Orion-1 an ai chatbot",
    "No I cant code, but I'm always learning",
    "Bye! See you later. <EOS>"
]

bigram_dict = {}
for sentence in outputs:
    words = sentence.split()
    for i in range(len(words) - 1):
        if words[i] not in bigram_dict:
            bigram_dict[words[i]] = []
        bigram_dict[words[i]].append(words[i + 1])

def generate_bigram_response(user_input, max_words=20):
    matched_index = None
    for i, phrase in enumerate(inputs):
        if phrase in user_input.lower():
            matched_index = i
            break
    
    if matched_index is not None:
        sentence = [outputs[matched_index].split()[0]]
    else:
        sentence = [random.choice(list(bigram_dict.keys()))]
    
    for _ in range(max_words):
        last_word = sentence[-1]
        next_words = bigram_dict.get(last_word, ["<EOS>"])
        next_word = random.choice(next_words)
        sentence.append(next_word)
        if next_word == "<EOS>":
            break
    return " ".join(sentence).replace("<EOS>", "").strip()

print("AI: Hi! I'm Orion-1. Type 'exit' to exit.")
while True:
    user_input = input("You: ")
    if "exit" in user_input.lower():
        print("AI:", generate_bigram_response("exit"))
        break
    print("AI:", generate_bigram_response(user_input))