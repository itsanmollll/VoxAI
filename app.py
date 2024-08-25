import whisper
model = whisper.load_model("base.en")
print("Whisper model loaded successfully!")

import whisper

model = whisper.load_model("base.en")
result = model.transcribe("mono_audio.wav", language="en"   )
text = result['text']
print("Transcribed Text:", text)

from transformers import pipeline

model = pipeline("text-generation", model="gpt-3")
response = model(text, max_length=50)
print("Generated Response:", response)


from transformers import pipeline

# Load the text-generation pipeline with GPT-2
model = pipeline("text-generation", model="gpt2")

# Example transcribed text from Chunk 2
text = "What is the weather like today?"

# Generate a response with a maximum of 50 tokens (adjust as needed)
response = model(text, max_length=50)
generated_text = response[0]['generated_text']
print("Generated Response:", generated_text)

response = model(text, max_length=50)  # Limit to 50 tokens

# Post-process to restrict output to 2 sentences
generated_text = response[0]['generated_text']
sentences = generated_text.split('.')
limited_response = '.'.join(sentences[:2]) + '.'  # Keep only the first two sentences
print("Limited Response:", limited_response)
