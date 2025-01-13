import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_features_with_gpt(transcript):
    prompt = f"""
    Your task is to read the following text which is an interview with a person and to summarize the key points that might be related to the depression of the person:
    {transcript}
    """
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7)
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("Error during API call:", e)
        return None

def read_transcript(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == "__main__":
    # Path to the transcribed text file
    transcript_path = "transcripts/300_AUDIO_transcript.txt"

    # Read the transcript
    transcript = read_transcript(transcript_path)
    if not transcript:
        print("Transcript is empty or not loaded correctly.")
    else:
        print("Transcript Loaded:", transcript[:100])  # Print first 100 characters

    # Extract features
    features = extract_features_with_gpt(transcript)

    # Print the extracted features
    print("Extracted Features:", features)