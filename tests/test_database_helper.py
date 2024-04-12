import pytest
from unittest.mock import Mock
import json 
from database_helper import (
    meta, 
    insert_email_record, 
    engine,
    check_message_id,
    dict_to_sqlalchemy_query)
from tests.jsons.test_database_helper_jsons import payload_1, payload_2
import datetime 
import sqlalchemy as db
from dateutil import parser


def test_create_database_table(init_database):
    assert meta.tables.get("emails").name == "emails"


@pytest.mark.parametrize("data", [
    {"subject": "Backend Engineer Assignment",
    "mail_from": "test@gmail.com",
    "mail_to": "testuser@gmail.com",
    "received_date": "Fri, 12 Apr 2024 20:34:48 +0800",
    "message_body": "This is a test email",
    "payload": payload_1,
    "message_id": "18ece5a6abe27125"
}])
def test_insert_email_record(init_database, data):
    
    insert_email_record(subject=data["subject"],
                        mail_from=data["mail_from"],
                        mail_to=data["mail_to"],
                        received_date=parser.parse(data["received_date"]).date(),
                        message_body=data["message_body"],
                        payload=json.dumps(data["payload"]),
                        message_id=data["message_id"])
    
    emails = meta.tables.get("emails")
    query = db.select(emails).where(emails.c.subject==data["subject"])
    conn = engine.connect()
    result = conn.execute(query)
    rows = result.fetchall()
    print(rows[0].email_received_date)
    assert rows[0].subject == data["subject"]
    assert rows[0].mail_from == data["mail_from"]
    assert rows[0].mail_to == data["mail_to"]
    assert rows[0].email_received_date == parser.parse(data["received_date"]).date()
    assert rows[0].body == data["message_body"]
    assert rows[0].payload == json.dumps(payload_1)
    assert rows[0].message_id == data["message_id"]
    meta.drop_all(engine)


@pytest.mark.parametrize("data, expected_result", [
    ({"subject": "Backend Engineer Assignment",
    "mail_from": "test@gmail.com",
    "mail_to": "testuser@gmail.com",
    "received_date": "2024-04-11",
    "message_body": "This is a test email",
    "payload": payload_1,
    "message_id": "18ece5a6abe27125"
    }, (False, True))
])
def test_check_message_id(init_database, data, expected_result):
    meta.create_all(engine)
    result = check_message_id(data['message_id'])
    assert result == expected_result[0]

    insert_email_record(subject=data["subject"],
                        mail_from=data["mail_from"],
                        mail_to=data["mail_to"],
                        received_date=parser.parse(data["received_date"]).date(),
                        message_body=data["message_body"],
                        payload=json.dumps(data["payload"]),
                        message_id=data["message_id"])
    
    result = check_message_id(data['message_id'])
    assert result == expected_result[1]
    meta.drop_all(engine)



@pytest.mark.parametrize("data", [
    ([{"subject": "Backend Engineer Assignment",
    "mail_from": "test@gmail.com",
    "mail_to": "testuser@gmail.com",
    "received_date": "2024-04-11",
    "message_body": "This is a test email",
    "payload": payload_1,
    "message_id": "18ece5a6abe27125"
    },
    {"subject": "Assignment Instructions",
    "mail_from": "Sakshi V. sakshiv@gmail.com",
    "mail_to": "Riya riya@gmail.com",
    "received_date": "2024-04-04",
    "message_body": "Please read the instructions carefully",
    "payload": payload_2,
    "message_id": "18ece5a6abe27145"
    }]),
])
def test_dict_to_sqlalchemy_query(init_database, data):
    group = { "select":"any", 
              "rules": [    {"field":"email_received_date",
                            "condition":"less than",
                            "value":"1",
                            "unit":"days"
                            },
                            {"field":"subject",
                            "condition":"does not equal",
                            "value":"Free Online Scuba Refresher Course, eCard + More"
                            },
                            {
                                "field": "mail_from",
                                "value": "swamis71@gmail.com",
                                "condition": "equal to"
                            }
                        ], 
              "action": { "command":"mark", "value":"unread" }  
            }
    meta.create_all(engine)
    for record in data:
        insert_email_record(subject=record["subject"],
                            mail_from=record["mail_from"],
                            mail_to=record["mail_to"],
                            received_date=parser.parse(record["received_date"]).date(),
                            message_body=record["message_body"],
                            payload=json.dumps(record["payload"]),
                            message_id=record["message_id"])
    message_ids = dict_to_sqlalchemy_query(group)
    assert len(message_ids) == 2
    meta.drop_all(engine)
        

    