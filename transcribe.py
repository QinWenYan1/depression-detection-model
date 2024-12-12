import whisper # type: ignore
import os
from pathlib import Path

def transcribe_audio(audio_path, model_size="base", output_dir="transcripts"):
    """
    Transcribe audio file using Whisper model
    
    Args:
        audio_path (str): Path to the audio file
        model_size (str): Size of the Whisper model ('tiny', 'base', 'small', 'medium', 'large')
        output_dir (str): Directory to save the transcript
    
    Returns:
        str: Transcribed text
    """
    try:
        # Load Whisper model
        print(f"Loading Whisper {model_size} model...")
        model = whisper.load_model(model_size)
        
        # Check if audio file exists
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
            
        # Transcribe audio
        print("Transcribing audio...")
        result = model.transcribe(audio_path)
        
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Generate output filename
        audio_filename = os.path.basename(audio_path)
        output_filename = f"{os.path.splitext(audio_filename)[0]}_transcript.txt"
        output_path = os.path.join(output_dir, output_filename)
        
        # Save transcript with one segment per line
        with open(output_path, "w", encoding="utf-8") as f:
            for segment in result['segments']:
                f.write(segment['text'].strip() + '\n')
            
        print(f"Transcript saved to: {output_path}")
        return result['text']
        
    except Exception as e:
        print(f"Error during transcription: {str(e)}")
        raise

if __name__ == "__main__":
    # Configuration
    AUDIO_PATH = "../E-DAIC/data/300_P/300_AUDIO.wav"
    MODEL_SIZE = "base"  # you can change to 'tiny', 'base', 'small', 'medium', 'large'
    OUTPUT_DIR = "transcripts"
    
    # Run transcription
    transcript = transcribe_audio(AUDIO_PATH, MODEL_SIZE, OUTPUT_DIR)
    
    # Only print success message
    print("\nTranscription completed successfully!") 