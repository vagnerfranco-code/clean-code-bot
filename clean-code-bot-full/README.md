# Clean Code Bot

AI-powered CLI tool that refactors code using SOLID principles.

## Features
- Code analysis (Chain of Thought)
- Automated refactoring
- Prompt injection protection
- CLI interface

## Setup

```bash
pip3 install -r requirements.txt
cp .env.example .env
```

## Usage

```bash
python3 -m clean_code_bot.cli examples/before/example.py
```

## Run Tests

```bash
python3 -m pytest
```
