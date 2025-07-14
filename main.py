# Entry point
from transcribe import transcribe_audio
from summarize import generate_summary
import json
from datetime import datetime

def main():
    audio_path = "sample_call.wav"  # Replace with actual call recording or use mic input
    transcript = transcribe_audio(audio_path)
    
    if transcript:
        summary = generate_summary(transcript)
        
        log = {
            "timestamp": datetime.now().isoformat(),
            "transcript": transcript,
            "summary": summary
        }
        
        with open("logs/summary_log.json", "a") as f:
            json.dump(log, f)
            f.write("\n")

        print("\n=== Transcript ===\n", transcript)
        print("\n=== Summary ===\n", summary)
    else:
        print("Failed to transcribe audio.")

if __name__ == "__main__":
    main()
