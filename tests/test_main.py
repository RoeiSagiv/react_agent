import pytest
from react_agent.main import greet

def test_greet():
    assert greet("World") == "Hello, World!"
