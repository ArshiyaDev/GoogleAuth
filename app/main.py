

from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.templating import Jinja2Templates


app = FastAPI()



oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=email openid profile",
    tokenUrl="https://accounts.google.com/o/oauth2/token",
)



templates = Jinja2Templates(directory="templates")




def get_current_user(token: str = Depends(oauth2_scheme)):
    # You can implement logic here to verify the token and fetch user information
    # For simplicity, this example just returns the token
    return token




@app.get("/login", response_class=HTMLResponse)
async def login_route(request: Request, current_user: str = Depends(get_current_user)):
    return templates.TemplateResponse("login.html", {"request": request})