from setuptools import setup, find_packages

setup(
    name="clean-code-bot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "click",
        "groq"
    ],
    entry_points={
        "console_scripts": [
            "clean-code-bot=clean_code_bot.cli:main"
        ]
    }
)
