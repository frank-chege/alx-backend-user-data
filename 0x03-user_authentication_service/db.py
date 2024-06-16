#!/usr/bin/env python3

"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError, SQLAlchemyError
from typing import Any
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
    
    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a user's credentials to the db and returns the user instance"""
        new_user = User(email=email, hashed_password=hashed_password)
        try:
            self._session.add(new_user)
            self._session.commit()
        except SQLAlchemyError as e:
            self._session.rollback()
            print(f"Error adding user: {e}")
            raise
        return new_user
    
    def find_user_by(self, **kwargs: Any) -> User:
        """Fetches data based on the arguments passed"""
        try:
            result = self._session.query(User).filter_by(**kwargs).first()
            if result is None:
                raise NoResultFound
        except NoResultFound:
            raise
        except SQLAlchemyError as e:
            print(f"Error querying user: {e}")
            raise InvalidRequestError
        return result
