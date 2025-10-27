import random
import json
import os

# --- Settings ---
N_GRAM_SIZE = 3
MARKOV_FILE = 'orion/model.json'
TRAINING_DATA_FILE = 'orion/training_data.json'

def build_ngram_dict(outputs, n_gram_size):
    ngram_dict = {}
    for sentence in outputs:
        words = sentence.split()
        if len(words) >= n_gram_size:
            for i in range(len(words) - (n_gram_size - 1)):
                history = tuple(words[i:i + n_gram_size - 1])
                next_word = words[i + n_gram_size - 1]
                if history not in ngram_dict:
                    ngram_dict[history] = []
                ngram_dict[history].append(next_word)
    return ngram_dict

def save_markov_json(ngram_dict):
    serializable_dict = {str(k): v for k, v in ngram_dict.items()}
    with open(MARKOV_FILE, 'w') as f:
        json.dump(serializable_dict, f)

def load_markov_json():
    try:
        with open(MARKOV_FILE, 'r') as f:
            serializable_dict = json.load(f)
        return {eval(k): v for k, v in serializable_dict.items()}
    except (FileNotFoundError, json.JSONDecodeError):
        return None

try:
    with open(TRAINING_DATA_FILE, 'r') as f:
        training_dict = json.load(f)
    inputs = list(training_dict.keys())
    outputs = list(training_dict.values())
except FileNotFoundError:
    print(f"Error: '{TRAINING_DATA_FILE}' not found. Exiting.")
    exit()

ngram_dict = load_markov_json()
if not ngram_dict:
    print(f"'{MARKOV_FILE}' not found or is empty. Building Markov chain from scratch...")
    ngram_dict = build_ngram_dict(outputs, N_GRAM_SIZE)
    save_markov_json(ngram_dict)
    print(f"Markov chain built and saved to '{MARKOV_FILE}'.")
else:
    print(f"Markov chain loaded from '{MARKOV_FILE}'.")

def generate_ngram_response(user_input, max_words=20):
    matched_index = None
    for i, phrase in enumerate(inputs):
        if phrase in user_input.lower():
            matched_index = i
            break
    
    sentence = []
    if matched_index is not None:
        response_words = outputs[matched_index].split()
        if len(response_words) >= N_GRAM_SIZE:
            sentence = response_words[:N_GRAM_SIZE - 1]
        else:
            return " ".join(response_words).replace("<EOS>", "").strip()

    if not sentence and ngram_dict:
        current_context = random.choice(list(ngram_dict.keys()))
        sentence = list(current_context)
    elif not sentence and not ngram_dict:
        return ""

    for _ in range(max_words):
        current_context = tuple(sentence[-(N_GRAM_SIZE - 1):]) if N_GRAM_SIZE > 1 else (sentence[-1],)
        next_words = ngram_dict.get(current_context, [])
        
        if not next_words:
            sentence.append("<EOS>")
            break
        
        next_word = random.choice(next_words)
        sentence.append(next_word)
        
        if next_word == "<EOS>":
            break
    
    return " ".join(sentence).replace("<EOS>", "").strip()

print(f"Hello I'm Orion-1 ask me anything.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("AI:", generate_ngram_response("bye"))
        break
    print("AI:", generate_ngram_response(user_input))