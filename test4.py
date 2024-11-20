import pytest
from main4 import init_db, add_user, get_user

@pytest.fixture
def db_conn():
   conn = init_db()
   yield conn
   conn.close()

def test_add_or_get_user(db_conn):
   add_user(db_conn, "Sasha", 29)
   user = get_user(db_conn, "Sasha")
   assert user == (1, "Sasha", 29)

   add_user(db_conn, "Anna", 55)
   user = get_user(db_conn, "Anna")
   assert user == (2, "Anna", 55)

   add_user(db_conn, "Kate", 28)
   user = get_user(db_conn, "Kate")
   assert user == (3, "Kate", 28)

