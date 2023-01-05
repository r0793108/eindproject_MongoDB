from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

#    items = relationship("Item", back_populates="owner")


#class Item(Base):
#    __tablename__ = "items"

#    id = Column(Integer, primary_key=True, index=True)
#    title = Column(String, index=True)
#    description = Column(String, index=True)
#    owner_id = Column(Integer, ForeignKey("users.id"))

#    owner = relationship("User", back_populates="items")


class Speler(Base):
    __tablename__ = "spelers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    HasChampionsLeague = Column(Boolean, default=False)
    club_id = Column(Integer, ForeignKey("teams.id"))

    club = relationship("Team", back_populates="spelers")


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    HasWonChampionsLeague = Column(Boolean, default=False)
    ChampionsYears = Column(String)

    spelers = relationship("Speler", back_populates="club")