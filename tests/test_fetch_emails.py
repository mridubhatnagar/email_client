from fetch_email import process_email_headers, process_email_body
from unittest.mock import Mock, MagicMock
from tests.jsons.test_database_helper_jsons import payload_1, payload_2
from tests.jsons.test_fetch_emails_json import multipart_alertnative
import pytest


@pytest.mark.parametrize("data, expected_result", [
    (payload_1['headers'], {"subject": "3-2-1: What top performers do, and how to deal with critics and detractors", 
                            "mail_from": "test@gmail.com", 
                            "date": "Thu, 11 Apr 2024 18:10:15 +0000 (UTC)", 
                            "mail_to": "testuser@gmail.com"}),
    (payload_2['headers'], {
        "subject": "Adventure Awaits!",
        "mail_from": "test@gmail.com",
        "date": "Thu, 11 Apr 2024 18:10:15 +0000 (UTC)",
        "mail_to": "riya@gmail.com"})
    ])
def test_process_email_headers(data, expected_result):
    assert process_email_headers(data) == expected_result



@pytest.mark.parametrize("data, expected_result", [
    (payload_1, "This is test email"),
    (payload_2, "Please read the instructions carefully"),
    (multipart_alertnative, "<h1>Hello World</h1>")
])
def test_process_email_body(data, expected_result):
    assert process_email_body(data) == expected_result