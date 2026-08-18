from Rough.FirstTest import printIlovePython


def test_string_output(capsys):
    print("Hello, World!")
    captured = capsys.readouterr()

    string_output = printIlovePython("Python")
    
    assert string_output == "I love Python!"