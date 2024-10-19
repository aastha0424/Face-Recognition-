import os
from extract_audio import extract_audio
from transcribe_audio import transcribe_audio
from correct_transcription import correct_transcription
from generate_audio import text_to_speech
from sync_audio_video import sync_audio_with_video

if __name__ == "__main__":
    video_file = 'input_video.mp4'
    
    # Step 1: Extract Audio
    extract_audio(video_file, 'extracted_audio.wav')
    
    # Step 2: Transcribe Audio
    transcription = transcribe_audio('extracted_audio.wav')
    with open('transcription.txt', 'w') as f:
        f.write(transcription)

    # Step 3: Correct Transcription
    corrected_text = correct_transcription(transcription)
    with open('corrected_text.txt', 'w') as f:
        f.write(corrected_text)

    # Step 4: Convert Corrected Text to Speech
    text_to_speech(corrected_text, 'output_audio.mp3')

    # Step 5: Sync Audio with Video
    sync_audio_with_video(video_file, 'output_audio.mp3', 'output_video.mp4')