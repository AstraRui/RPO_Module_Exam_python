from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from core.logging_config import logger  
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Incident(Base):
    __tablename__ = "incidents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    status = Column(String, default="open")

Base.metadata.create_all(bind=engine)

app = FastAPI(title="NexusMonitor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/incidents") # Повеселись, но сделали логирование
def get_incidents(db: Session = Depends(get_db)):
    logger.debug("Получен запрос GET /api/incidents. Инициализация запроса к БД.")
    
    try:
        incidents = db.query(Incident).all()
        
        if not incidents:
            logger.warning("Запрос к БД выполнен успешно, но таблица incidents пуста.")
            return {"status": "success", "data": []}
            
        logger.info(f"Успешно получено инцидентов из базы: {len(incidents)}")
        return {"status": "success", "data": incidents}
        
    except Exception as e:
        logger.error(f"Исключение при получении списка инцидентов: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Внутренняя ошибка сервера")