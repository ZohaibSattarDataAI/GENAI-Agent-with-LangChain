from youtube_transcript_api import YouTubeTranscriptApi

video_id = "cFnqX6V21h4"

transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

for t in transcript_list:
    print(t.language)
    print(t.language_code)
    print(t.is_generated)

    try:
        data = t.fetch()
        print("SUCCESS")
        print(data[:5])
    except Exception as e:
        print(type(e).__name__)
        print(e)