#!/usr/bin/python3
""" Get a state """


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    s_tate = session.query(State).filter(State.name == argv[4]).first()

    if s_tate:
        print("{}".format(s_tate.id))
    else:
        print("Not found")
    session.close()
