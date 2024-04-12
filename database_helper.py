import sqlalchemy as db
import datetime
from dateutil.relativedelta import relativedelta
import os

DATABASE_NAME = 'email'
TABLE_NAME = 'emails'
env = os.getenv("ENV")
if env == "local":
    DATABASE_URI = 'sqlite:///email.db'
elif env == "test":
    DATABASE_URI = 'sqlite:///:memory:'



engine = db.create_engine(DATABASE_URI)
meta  =db.MetaData()
meta.reflect(bind=engine)



def create_database_table():
    
    emails = db.Table(
        f'{TABLE_NAME}', meta,
        db.Column('id', db.Integer, primary_key=True),
        db.Column('created_at', db.DateTime, server_default=db.func.now(), nullable=False),
        db.Column('updated_at', db.DateTime, server_default=db.func.now(), nullable=False),
        db.Column('message_id', db.String),
        db.Column('email_received_date', db.Date, nullable=False),
        db.Column('mail_from', db.String),
        db.Column('mail_to', db.String),
        db.Column('subject', db.String),
        db.Column('body', db.Text),
        db.Column('payload', db.String)
    )
    meta.create_all(engine) 


def insert_email_record(**kwargs):
    email_table = meta.tables[TABLE_NAME]

    subject = kwargs.get("subject")
    mail_from = kwargs.get("mail_from")
    mail_to = kwargs.get("mail_to")
    if "received_date" in kwargs:
       date = kwargs.get("received_date")
    body = kwargs.get("message_body")
    payload = kwargs.get("payload")
    message_id = kwargs.get("message_id")   
    
    insert_command = email_table.insert().values(subject=subject, 
                                mail_from=mail_from,
                                mail_to=mail_to,
                                email_received_date=date,
                                body=body,
                                payload=payload,
                                message_id = message_id
                                )
    conn = engine.connect()
    result = conn.execute(insert_command)
    conn.commit()
    conn.close()


def check_message_id(message_id):
    email_table = meta.tables[TABLE_NAME]
    query = db.select(email_table).where(email_table.c.message_id == message_id)
    conn = engine.connect()
    result = conn.execute(query)
    rows = result.fetchall()
    conn.close()
    for row in rows:
        return True
    return False


def dict_to_sqlalchemy_query(group):
    email_table = meta.tables[TABLE_NAME]
    query = db.select(email_table.c.message_id)
    message_ids = []

    conjunction = group["select"]
    filter_dicts = group["rules"]
    
    filter_conditions = []
    for filter_dict in filter_dicts:
        if 'field' in filter_dict and 'value' in filter_dict:
            field_name = filter_dict['field']
            value = filter_dict['value']

            if field_name == 'email_received_date':
                unit = filter_dict['unit']
                if unit == "months":
                    days = 0
                    months = int(value)
                elif unit == "days":
                    months = 0
                    days = int(value)

                value = datetime.date.today() - relativedelta(days=days, months=months)

            if filter_dict['condition'] == 'contains':
                filter_conditions.append(db.text("' ' || {} || ' ' like '%{}%'".format(email_table.columns[field_name], value)))
            elif filter_dict['condition'] == 'does not contains':
                filter_conditions.append(db.text("' ' || {} || ' ' not like '%{}%'".format(email_table.columns[field_name], value)))
            elif filter_dict['condition'] == 'equal to':
                filter_conditions.append(email_table.columns[field_name] == value)
            elif filter_dict['condition'] == 'does not equal':
                filter_conditions.append(email_table.columns[field_name] != value)
            elif field_name == 'email_received_date' and filter_dict['condition'] == 'less than':
                filter_conditions.append(email_table.columns[field_name] >= value)
            elif field_name == 'email_received_date' and filter_dict['condition'] == 'greater than':
                filter_conditions.append(email_table.columns[field_name] <= value)

    if filter_conditions:
        if conjunction == "all":
            query = query.where(db.and_(*filter_conditions))
        elif conjunction == "any":
            query = query.where(db.or_(*filter_conditions))

        conn = engine.connect()
        result = conn.execute(query)
        rows = result.fetchall()
        conn.close()
        for row in rows:
            message_ids.append(row.message_id)
    return message_ids

