import pytest
from fetch_email import format_received_date
import sys
from datetime import datetime 
from tests.jsons.test_utils_jsons import (
    missing_select,
    missing_field,
    invalid_command,
    valid_rule,
    invalid_condition
)
from utils import validate_rules

@pytest.mark.parametrize("date, expected_result", [
    ("Thu, 11 Apr 2024 18:10:15 +0000 (UTC)", '2024-04-11'),
    ("Thu, 11 Apr 2024 18:10:15 +0000",'2024-04-11'),
    ("2024-04-11", '2024-04-11')
])
def test_format_received_date(date, expected_result):
    date = format_received_date(date)
    assert date == datetime.strptime(expected_result, "%Y-%m-%d").date()


@pytest.mark.parametrize("data, expected_result", [
    (missing_select, False),
    (missing_field, False),
    (invalid_command, False),
    (valid_rule, True),
    (invalid_condition, False)
])
def test_validate_rules(data, expected_result):
    assert validate_rules(data) == expected_result
    

 



