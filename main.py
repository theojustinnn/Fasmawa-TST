from fastapi import FastAPI

import uvicorn

# Routers yang digunakan
from auth import routers as AuthRouter
from user import routers as UserRouter
from fasilitas import routers as FasilitasRouter
from fasilitas import routers2 as KeramaianRouter
from lokasi import routers as LokasiRouter
from listfasilitas import routers as ListRouter


app = FastAPI()

# Include semua routers
app.include_router(AuthRouter.router)
app.include_router(UserRouter.router)
app.include_router(FasilitasRouter.router)
app.include_router(KeramaianRouter.router)
app.include_router(LokasiRouter.router)
app.include_router(ListRouter.router)

@app.get("/")
async def home():
	return {"Selamat Datang di Fasmawa ITB" : "Silahkan login terlebih dahulu"}

if __name__ == '__main__':
	uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
