import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter, TextFormatter


def _main(videoId: str) -> str:
    transcript = YouTubeTranscriptApi.get_transcript(videoId)
    return transcript


def getJson(videoId: str) -> str:
    """
    Raises:
        youtube_transcript_api._errors.TranscriptsDisabled: If transcript is disabled or the video is not found
    """
    formatter = JSONFormatter()
    transcript = _main(videoId)
    json_formatted = formatter.format_transcript(transcript, indent=2)
    return json_formatted


def getRaw(videoId: str) -> str:
    """
    Raises:
        youtube_transcript_api._errors.TranscriptsDisabled: If transcript is disabled or the video is not found
    """
    formatter = TextFormatter()
    transcript = _main(videoId)
    json_formatted = formatter.format_transcript(transcript)
    return json_formatted
