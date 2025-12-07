from models.config import get_responder
from utils.logger import log_line
def compress(text: str, max_chars: int = 500) -> str:
    if not text: return ''
    responder = get_responder()
    try:
        prompt = f"Summarize in 2-3 sentences: {text}"
        resp = responder(prompt)
        if resp.startswith('[DUMMY]'):
            return (text[:max_chars] + '...') if len(text) > max_chars else text
        return resp[:max_chars]
    except Exception as e:
        log_line('Compressor error: ' + str(e))
        return (text[:max_chars] + '...') if len(text) > max_chars else text
