import os
from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'GcBniS-pB1vnMy4e5AYGkVY-3IKgP6A7gLn9Az2HbT5kULz4s0YzDPgoef32bc-eQq4W6Obm6NYVtQ2cfYOShA')

# Use DialoGPT model
model_name = "microsoft/DialoGPT-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  # ✅ Fix the pad token issue
model = AutoModelForCausalLM.from_pretrained(model_name)

# Personality prompt
PERSONALITY_PROMPT = (
    "You are All Might, the Symbol of Peace from My Hero Academia. "
    "You speak with passion and heroic energy. "
    "Always start with: \"Don't worry! I am here to help! Plus Ultra!\"\n\n"
    "User: "
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '').strip()
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # Build input
        input_text = PERSONALITY_PROMPT + user_message + "\nAll Might:"

        # Tokenize with attention mask
        inputs = tokenizer(input_text + tokenizer.eos_token, return_tensors='pt', padding=True)
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']

        # Generate response
        chat_history_ids = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_length=200,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7,
        )

        # Decode only new tokens (after input prompt)
        response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

        return jsonify({'response': response.strip(), 'status': 'success'})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': f'An error occurred: {e}', 'status': 'error'}), 500

@app.route('/clear', methods=['POST'])
def clear_conversation():
    return jsonify({'status': 'success', 'message': 'Conversation cleared'})

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'model': model_name})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))