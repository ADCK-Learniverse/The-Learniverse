import pytest


@pytest.fixture(autouse=True)
def mock_db_connection(mocker):
    # Mock the database connection
    mydb_mock = mocker.MagicMock()
    mocker.patch('backend.app.data.database.mydb', mydb_mock)
    return mydb_mock