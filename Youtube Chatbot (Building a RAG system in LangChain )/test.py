from youtube_transcript_api import YouTubeTranscriptApi

video_id = "cFnqX6V21h4"

transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

for t in transcript_list:
    print("Fetching:", t.language)

    try:
        transcript = t.fetch()
        print("Success")
        print(transcript[:3])
    except Exception as e:
        print(type(e).__name__)
        print(e)