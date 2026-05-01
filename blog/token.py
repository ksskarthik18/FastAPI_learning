from datetime import datetime,timedelta
from typing import Optional
from jose import JWTError,jwt
from . import schemas


ALGORITHM= "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES =30
SECRET_KEY = ""

def create_access_token(data : dict , expires_delta : Optional[timedelta]=None):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    
    to_encode.update({'exp':expire})
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm =ALGORITHM)
    return encode_jwt

def verify_token(token : str,credentials_exception):
    try :
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email : str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception

