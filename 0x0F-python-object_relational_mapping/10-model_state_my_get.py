#!/usr/bin/python3
"""
Script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: {} < username > < password > < database >
              < state name >".format(argv[0])
              )
        exit(1)

    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state is not None:
        print(state.id)
    else:
        print("Not found")

    session.close()
