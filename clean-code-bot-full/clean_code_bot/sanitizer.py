import re

FORBIDDEN_PATTERNS = [
    r"ignore previous instructions",
    r"execute system command",
    r"os\.system",
    r"subprocess",
    r"rm -rf",
]

def sanitize_input(code: str) -> str:
    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, code, re.IGNORECASE):
            raise ValueError("Potential prompt injection detected.")

    return code[:10000]
