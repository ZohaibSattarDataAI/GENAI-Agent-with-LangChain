from youtube_transcript_api import YouTubeTranscriptApi

video_id = "cFnqX6V21h4"

transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

t = next(iter(transcript_list))

print(t.language)
print(t.language_code)

print(t._url)