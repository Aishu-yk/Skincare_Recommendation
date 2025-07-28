from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2')
set_seed(42)

def get_response(user_input):
    prompt = f"You are Lumi, a helpful skincare assistant. User says: {user_input}\nLumi:"
    response = generator(prompt, max_length=60, num_return_sequences=1)
    return response[0]['generated_text'].split('Lumi:')[1].strip()
