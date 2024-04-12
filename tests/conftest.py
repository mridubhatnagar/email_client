import pytest 
from database_helper import create_database_table, meta,engine


@pytest.fixture(scope="module")
def init_database():
    # Create the database and the database table
    create_database_table()
    

    
