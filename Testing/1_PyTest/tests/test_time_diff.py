from datetime import datetime, timezone
from functionality.Time_difference import calc_diff


def test_should_pass_for_end_time_equal_None():
    case = {
        'start_time': '2021-11-03T09:22:28+00:00',
        'end_time': None
    }
    start_time_obj = datetime.fromisoformat(case['start_time'])
    end_time_obj = datetime.now(timezone.utc)

    result = calc_diff(case)
    expected = (end_time_obj - start_time_obj).total_seconds()

    assert result == expected


def test_should_pass_for_end_time_equal_time():
    case = {
        'start_time': '2021-11-03T09:22:28+00:00',
        'end_time': '2021-12-03T09:22:28+00:00'
    }
    start_time_obj = datetime.fromisoformat(case['start_time'])
    end_time_obj = datetime.fromisoformat(case['end_time'])

    result = calc_diff(case)
    expected = (end_time_obj - start_time_obj).total_seconds()

    assert result == expected

