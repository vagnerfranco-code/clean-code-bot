from clean_code_bot.prompts import REFACTOR_PROMPT
from clean_code_bot.llm_client import call_llm

def refactor_code(code: str, analysis: str) -> str:
    prompt = REFACTOR_PROMPT.format(code=code, analysis=analysis)
    return call_llm(prompt)
