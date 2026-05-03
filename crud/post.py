from sqlalchemy.orm import Session
from models.post import Post

def get_posts(db: Session):
    return db.query(Post).all()

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def create_post(db: Session, title: str, content: str):
    post = Post(title=title, content=content)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def update_post(db: Session, post_id: int, title: str, content: str):
    post = get_post(db, post_id)
    if post:
        post.title = title
        post.content = content
        db.commit()
        db.refresh(post)
    return post

def delete_post(db: Session, post_id: int):
    post = get_post(db, post_id)
    if post:
        db.delete(post)
        db.commit()
    return post