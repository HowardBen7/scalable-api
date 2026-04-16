from pydantic import BaseModel

# Defines what user data should look like when the API sends it back
# This is the "safe" version, so it does not include the password
class UserResponse(BaseModel):
    name: str
    email: str


# Defines what data the API expects to receive when creating a user
# This includes password because the client must send it
class UserCreate(BaseModel):
    name: str
    email: str
    password: str