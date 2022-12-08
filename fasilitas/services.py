from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from . import models, schemas
from lokasi import models as lokmodels
from listfasilitas import models as lfasmodels

# Create data penggunaan fasilitas baru
async def create_fasilitas(fasilitas: schemas.CreateFasilitas, db:Session) -> schemas.GetFasilitas:
	new_fasilitas = models.Fasilitas(**fasilitas.dict())
	cek_fasilitas = db.query(lfasmodels.ListFasilitas.nama).filter(lfasmodels.ListFasilitas.nama == new_fasilitas.nama).all()

	print(cek_fasilitas)
	if cek_fasilitas == []:
		raise HTTPException(status_code=400, detail='Fasilitas invalid')
	db.add(new_fasilitas)
	db.commit()

	db.refresh(new_fasilitas)
	return schemas.GetFasilitas.from_orm(new_fasilitas)

# Update data penggunaan fasilitas
async def update_fasilitas(nama: str, hari: str, waktu: str, pengguna: str, db:Session) -> schemas.GetFasilitas:
	cek_fasilitas = db.query(models.Fasilitas.nama).\
		filter(models.Fasilitas.nama == nama, models.Fasilitas.hari == hari, models.Fasilitas.pengguna == pengguna).\
			all()
	if cek_fasilitas == []:
		raise HTTPException(status_code=400, detail='Fasilitas invalid')
	updated_fasilitas = db.query(models.Fasilitas).\
		filter(models.Fasilitas.nama == nama, models.Fasilitas.hari == hari, models.Fasilitas.pengguna == pengguna).\
			update({models.Fasilitas.waktu: waktu})
	db.commit()
	return {"Status" : "Berhasil Update"}

# Delete data penggunaan fasilitas
async def delete_fasilitas(nama: str, hari: str, waktu: str, pengguna: str, db:Session) -> schemas.GetFasilitas:
	cek_fasilitas = db.query(models.Fasilitas.nama).\
		filter(models.Fasilitas.nama == nama, models.Fasilitas.hari == hari, models.Fasilitas.waktu == waktu, models.Fasilitas.pengguna == pengguna).\
			all()
	if cek_fasilitas == []:
		raise HTTPException(status_code=400, detail='Fasilitas invalid')
	deleted_fasilitas = db.query(models.Fasilitas).\
		filter(models.Fasilitas.nama == nama, models.Fasilitas.hari == hari, models.Fasilitas.pengguna == pengguna, models.Fasilitas.waktu == waktu).\
			delete(synchronize_session=False)
	db.commit()
	return {"Status" : "Berhasil Menghapus"}

# Get semua penggunaan fasilitas
async def get_all_fasilitas(db: Session) -> List[schemas.GetFasilitas]:
	fasilitas = db.query(models.Fasilitas).\
		order_by(models.Fasilitas.hari.desc()).\
			all()
	if fasilitas is None:
		return {"Details" : "Tidak ada penggunaan fasilitas saat ini"}
	return list(map(schemas.GetFasilitas.from_orm, fasilitas))

# Get penggunaan fasilitas berdasarkan lokasi
async def get_lokasi_fasilitas(lokasi: str, db: Session) -> List[schemas.GetFasilitas]:
	fasilitas = db.query(models.Fasilitas).filter(models.Fasilitas.lokasi == lokasi).all()
	print(fasilitas)
	if fasilitas is None:
		return {"Details" : "Tidak ada penggunaan fasilitas pada lokasi ini"}
	return list(map(schemas.GetFasilitas.from_orm, fasilitas))

# Get keramaian lokasi
async def get_keramaian(lokasi: str, hari: str, waktu: str, db: Session):
	cek_fasilitas = db.query(models.Fasilitas.nama).\
		filter(lokmodels.Lokasi.nama == lokasi).\
			all()
	if cek_fasilitas == []:
		raise HTTPException(status_code=400, detail='Lokasi invalid')
	jumlah = db.query(func.sum(models.Fasilitas.jumlah)).\
		where(models.Fasilitas.lokasi == lokasi, models.Fasilitas.hari == hari, models.Fasilitas.waktu == waktu).\
			all()

	print(jumlah)
		
	if (jumlah[0][0] == None):
		return {"Perkiraan Keramaian" : 0}
	intjumlah = jumlah[0][0]
	return {"Perkiraan Keramaian" : intjumlah}

# Get keramaian lokasi berdasarkan fasilitas
async def get_keramaian_fasilitas(nama: str, hari: str, waktu: str, db: Session):
	cek_fasilitas = db.query(models.Fasilitas.nama).\
		filter(lfasmodels.ListFasilitas.nama == nama).\
			all()
	if cek_fasilitas == []:
		raise HTTPException(status_code=400, detail='Fasilitas invalid')
	lokasi = db.query(models.Fasilitas.lokasi).\
		where(models.Fasilitas.nama == nama).\
			all()

	print(lokasi)

	if (lokasi[0][0] == None):
		return {"Error" : "Fasilitas tidak valid"}
	return await get_keramaian(lokasi=lokasi[0][0], hari=hari, waktu=waktu, db=db)

# Get rekomendasi fasilitas
async def get_rekomendasi(jumlah: int, hari:str, waktu:str, db: Session):
	fasilitas = db.query(func.sum(models.Fasilitas.jumlah), models.Fasilitas.nama, models.Fasilitas.lokasi).\
		where(models.Fasilitas.hari == hari and models.Fasilitas.waktu == waktu).\
			group_by(models.Fasilitas.lokasi).\
			having(models.Fasilitas.waktu == waktu).\
			order_by(func.sum(models.Fasilitas.jumlah)).\
			all()
	
	i = 0
	while i < len(fasilitas):
		jumlahbaru = fasilitas[i][0] + jumlah
		kapasitas = db.query(func.sum(lokmodels.Lokasi.kapasitas)).\
			where(lokmodels.Lokasi.nama == fasilitas[i][2]).all()

		listfasilitas = db.query(lfasmodels.ListFasilitas.nama).\
			where(lfasmodels.ListFasilitas.lokasi == fasilitas[i][2]).all()

		if (jumlahbaru <= kapasitas[0][0]):
			j = 0
			while j < len(listfasilitas):
				if (listfasilitas[j][0] != fasilitas[i][1]):
					return {"Rekomendasi Fasilitas" : listfasilitas[j][0]}
				j+=1
			return {"Rekomendasi Fasilitas" : fasilitas[i-1][1]}
		i+=1
	
	fasilitaslain = db.query(lfasmodels.ListFasilitas.nama).\
		order_by(func.random()).\
			all()
	k = 0
	l = 0
	while k < len(fasilitaslain):
		while l < len(fasilitas):
			if (fasilitaslain[k][0] != fasilitas[l][1]):
				return {"Rekomendasi Fasilitas" : fasilitaslain[k][0]}
			l+=1
		k+=1

	return {"Rekomendasi Fasilitas" : "Tidak ada, silahkan datangi kantor Ditmawa atau DitSP"}
