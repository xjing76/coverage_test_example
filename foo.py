def foo():
    for i in range(10):
        if i < 10:
            print(1)
        else :
            continue
    return 5

def main():
    foo()


if __name__ == '__main__': # pragma: no cover
    main()

## test code

# To test:
# pip install pytest
# pytest script.py

# To test with coverage:
# put this file (script.py) in a directory by itself, say foo
# then from the parent directory of foo:
# pip install pytest-cov
# pytest --cov=foo foo/script.py

# To show missing lines
# pytest --cov=foo --cov-report=term-missing foo/script.py


