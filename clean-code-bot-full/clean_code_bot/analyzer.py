from clean_code_bot.prompts import ANALYSIS_PROMPT
from clean_code_bot.llm_client import call_llm

def analyze_code(code: str) -> str:
    prompt = ANALYSIS_PROMPT.format(code=code)
    return call_llm(prompt)
