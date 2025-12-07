import os
try:
    import openai
except Exception:
    openai = None
MODEL_NAME = os.getenv('OPENAI_MODEL', 'gpt-5')
API_KEY = os.getenv('OPENAI_API_KEY', '')
USE_OPENAI = os.getenv('USE_OPENAI', '') != '' and API_KEY
def get_responder():
    if openai and USE_OPENAI:
        openai.api_key = API_KEY
        def call_openai(prompt: str):
            try:
                resp = openai.Completion.create(engine=MODEL_NAME, prompt=prompt, max_tokens=512, temperature=0.2)
                return resp.choices[0].text.strip()
            except Exception as e:
                return '[OpenAI error] ' + str(e)
        return call_openai
    else:
        def dummy(prompt: str):
            return '[DUMMY] ' + (prompt.splitlines()[0][:140] if prompt else '...')
        return dummy
