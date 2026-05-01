from datetime import datetime,timedelta
from typing import Optional
import jwt

ALGORITHM= "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES =30
SECRET_KEY = ""

def create_access_token(data : dict , expires_delta : Optional[timedelta]=None):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    
    to_encode.update({'exp':expire})
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm =ALGORITHM)
    return encode_jwt
