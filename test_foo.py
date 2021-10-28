from foo import foo, main

def test_foo():
    assert foo() == 5


def test_main(capsys):
    main()
    captured = capsys.readouterr()