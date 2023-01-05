from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

import models
import schemas
import auth


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


#def get_items(db: Session, skip: int = 0, limit: int = 100):
#    return db.query(models.Item).offset(skip).limit(limit).all()


#def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#    db_item = models.Item(**item.dict(), owner_id=user_id)
 #   db.add(db_item)
  #  db.commit()
   # db.refresh(db_item)
    #return db_item


def get_speler(db: Session, speler_id: int):
    return db.query(models.Speler).filter(models.Speler.id == speler_id).first()


def get_speler_by_name(db: Session, name: str):
    return db.query(models.Speler).filter(models.Speler.name == name).first()


def get_spelers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Speler).offset(skip).limit(limit).all()


def create_speler(db: Session, speler: schemas.SpelerCreate):
    db_speler = models.Speler(name=speler.name)
    db.add(db_speler)
    db.commit()
    db.refresh(db_speler)
    return db_speler


def delete_speler(db: Session, speler: schemas.SpelerCreate):
    db_speler = models.Speler(name=speler.name)
    db.delete(db_speler)
    db.commit()
    db.refresh(db_speler)
    return db_speler


def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()


def get_team_by_name(db: Session, name: str):
    return db.query(models.Team).filter(models.Team.name == name).first()


def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Team).offset(skip).limit(limit).all()


def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(name=team.name, ChampionsYears=team.ChampionsYears)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team
