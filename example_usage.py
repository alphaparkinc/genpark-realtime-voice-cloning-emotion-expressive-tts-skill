from client import RealtimeVoiceCloningEmotionExpressiveTtsClient

def main():
    client = RealtimeVoiceCloningEmotionExpressiveTtsClient()
    res = client.generate_expressive_speech("Welcome to the 2026 AI Product Summit!", "ref.wav", "ENTHUSIASTIC")
    print(f"Duration: {res['audio_duration_sec']} seconds")
    print(f"Generated Audio URL: {res['generated_audio_url']}")

if __name__ == "__main__":
    main()
