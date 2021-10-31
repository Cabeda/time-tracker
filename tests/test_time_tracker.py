from time_tracker.log import Logger

logger = Logger()


def test_open_last_log():
    log_result = logger.get_logs(last_log=True, output=False)

    assert log_result is True or log_result is None


def test_show_last_log():
    log_result = logger.get_logs(last_log=True, output=True)

    return log_result  # Should be able to return the content
