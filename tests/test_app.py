import sys
import os
from unittest.mock import patch, MagicMock

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import pytest
from app import app


@pytest.fixture
def client():

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client



@patch("app.get_connection")
def test_home_page(mock_connection, client):

    # Fake database connection
    mock_conn = MagicMock()

    # Fake database cursor
    mock_cursor = MagicMock()

    # Fake database response
    mock_cursor.fetchall.return_value = [
        (1, "John", 5000)
    ]


    mock_conn.cursor.return_value = mock_cursor

    mock_connection.return_value = mock_conn


    response = client.get("/")


    assert response.status_code == 200
