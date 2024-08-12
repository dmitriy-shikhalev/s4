from unittest.mock import patch, Mock

from s4 import entrypoints


@patch('s4.entrypoints.app')
@patch('s4.entrypoints.Settings', return_value=Mock())
@patch('s4.entrypoints.uvicorn.run')
def test_router(run_mock, settings_mock, app_mock):
    entrypoints.router()

    settings_mock.assert_called_once_with()
    run_mock.assert_called_once_with(
        app_mock,
        host=settings_mock.return_value.host,
        port=settings_mock.return_value.port
    )