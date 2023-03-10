from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import crud
import models
import schemas
import auth
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/me", response_model=schemas.User)
def read_users_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = auth.get_current_active_user(db, token)
    return current_user


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


#@app.post("/users/{user_id}/items/", response_model=schemas.Item)
#def create_item_for_user(
 #   user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
#):
 #   return crud.create_user_item(db=db, item=item, user_id=user_id)


#@app.get("/items/", response_model=list[schemas.Item])
#def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
 #   items = crud.get_items(db, skip=skip, limit=limit)
  #  return items


@app.post("/teams/", response_model=schemas.Team)
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_team = crud.get_team_by_name(db, name=team.name)
    if db_team:
        raise HTTPException(status_code=400, detail="Team already registered")
    return crud.create_team(db=db, team=team)


@app.get("/teams/", response_model=list[schemas.Team])
def read_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    teams = crud.get_teams(db, skip=skip, limit=limit)
    return teams


@app.get("/teams/{team_id}", response_model=schemas.Team)
def read_team(team_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_team = crud.get_team(db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return db_team


@app.post("/spelers/", response_model=schemas.Speler)
def create_speler(speler: schemas.SpelerCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_speler = crud.get_speler_by_name(db, name=speler.name)
    if db_speler:
        raise HTTPException(status_code=400, detail="Speler already registered")
    return crud.create_speler(db=db, speler=speler)


@app.put("/spelers/", response_model=schemas.Speler)
async def create_speler(speler: schemas.SpelerCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_speler = crud.get_speler_by_name(db, name=speler.name)
    if db_speler:
        raise HTTPException(status_code=400, detail="Speler already registered")
    return crud.create_speler(db=db, speler=speler)


@app.get("/spelers/", response_model=list[schemas.Speler])
def read_spelers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    spelers = crud.get_spelers(db, skip=skip, limit=limit)
    return spelers


@app.get("/spelers/{speler_id}", response_model=schemas.Speler)
def read_speler(speler_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_speler = crud.get_speler(db, speler_id=speler_id)
    if db_speler is None:
        raise HTTPException(status_code=404, detail="Speler not found")
    return db_speler


@app.delete("/spelers/", response_model=schemas.Speler)
def delete_speler(speler: schemas.SpelerCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_speler = crud.get_speler_by_name(db, name=speler.name)
    return crud.create_speler(db=db, speler=speler)

