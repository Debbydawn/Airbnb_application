# import pytest
# import pandas as pd
# from User_code import dawn_airbnb


# def dawn_airbnb():
#     # Call the function being tested
#     result = average_price_location()
#     assert isinstance(result, list)

# if __name__ == '__main__':
#     pytest.main()
import pytest
from User_code import dawn_airbnb

def test_dawn_airbnb(monkeypatch):
    # Mock user input for choice 2
    monkeypatch.setattr('builtins.input', lambda _: '2')

    dawn_airbnb()

    # Add assertions for choice 2
    assert "What is your name?" in capsys.readouterr().out
    assert "Please enter your desired name: " in capsys.readouterr().out
    assert "Yes, USERNAME let's get to work." in capsys.readouterr().out
    assert "Option 2 selected." in capsys.readouterr().out

    # Mock user input for host_id
    monkeypatch.setattr('builtins.input', lambda _: '554519')

    dawn_airbnb()

    # Add assertions for host details
    assert "Enter the host ID: " in capsys.readouterr().out
    assert "Host Name: " in capsys.readouterr().out
    assert "Host Location: " in capsys.readouterr().out
    assert "Host Response Time: " in capsys.readouterr().out
    # Add more assertions to check other host details
    
