#!/usr/bin/python3

''' had lkatba smyathom '''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    ''' hdait arbar dyalo '''

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    ari_state = session.query(State).filter(State.id == '2').first()
    ari_state.name = 'New Mexico'
    session.commit()
    session.close()
