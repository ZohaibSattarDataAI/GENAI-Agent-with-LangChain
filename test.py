from youtube_transcript_api import YouTubeTranscriptApi

video_id = "cFnqX6V21h4"

try:
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    print("Available transcripts:")
    for transcript in transcript_list:
        print(
            transcript.language,
            transcript.language_code,
            transcript.is_generated
        )

except Exception as e:
    print(type(e).__name__)
    print(e)