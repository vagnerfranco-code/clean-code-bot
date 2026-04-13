ANALYSIS_PROMPT = """
You are a senior software engineer performing a code review.

Step 1: Understand the purpose of the code.
Step 2: Identify code smells and anti-patterns.
Step 3: Evaluate violations of SOLID principles.
Step 4: Suggest improvements.

Code:
{code}

Provide a structured analysis.
"""

REFACTOR_PROMPT = """
You are an expert software engineer.

Based on the following analysis:
{analysis}

Refactor the code to:
- Follow SOLID principles
- Improve readability and maintainability
- Add docstrings (or JSDoc if JavaScript)
- Keep functionality unchanged

Code:
{code}

Return ONLY the improved code.
"""
