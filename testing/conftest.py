import sys, os, inspect
import pytest

# Do some gymnastics to add the path to 'app.py'
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from app import MyApp

@pytest.fixture
def app():
    app = MyApp()
    return app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()