from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from services import post_service
from schemas.post import PostCreate, PostResponse

router = APIRouter(prefix="/posts", tags=["Posts"])

# DB 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[PostResponse])
def read_posts(db: Session = Depends(get_db)):
    return post_service.get_posts(db)

@router.get("/{post_id}", response_model=PostResponse)
def read_post(post_id: int, db: Session = Depends(get_db)):
    try:
        return post_service.get_post(db, post_id)
    except Exception:
        raise HTTPException(status_code=404, detail="Post not found")
    
@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
        return post_service.create_post(db, post)
    
@router.put("/{post_id}", response_model=PostResponse)
def update_post(post_id: int, post: PostCreate, db: Session = Depends(get_db)):
    try:
        return post_service.update_post(db, post_id, post)
    except Exception:
        raise HTTPException(status_code=404, detail="Post not found")

@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    try:
        post_service.delete_post(db, post_id)
        return {"message": "deleted"}
    except Exception:
        raise HTTPException(status_code=404, detail="Post not found")