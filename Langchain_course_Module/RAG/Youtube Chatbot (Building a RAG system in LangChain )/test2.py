from youtube_transcript_api import YouTubeTranscriptApi

video_id = "cFnqX6V21h4"

transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

print("Available transcripts:\n")

for t in transcript_list:
    print("Language:", t.language)
    print("Code:", t.language_code)
    print("Generated:", t.is_generated)
    print("----------------")