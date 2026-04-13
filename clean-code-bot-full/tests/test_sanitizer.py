from clean_code_bot.sanitizer import sanitize_input

def test_safe_input():
    assert sanitize_input("print('hello')")

def test_malicious_input():
    try:
        sanitize_input("os.system('rm -rf /')")
        assert False
    except ValueError:
        assert True
