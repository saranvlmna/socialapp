from fastapi import FastAPI
from routers.user.router import user_router
from routers.post.router import post_router
app=FastAPI()

app.include_router(user_router)
app.include_router(post_router)

@app.get("/")
async def root():
    return {"message":"hey social"}