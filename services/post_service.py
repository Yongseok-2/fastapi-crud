from sqlalchemy.orm import Session
from crud import post as post_crud
from schemas.post import PostCreate

def get_posts(db: Session):
    return post_crud.get_posts(db)

def get_post(db: Session, post_id: int):
    post = post_crud.get_post(db, post_id)
    if not post:
        raise Exception("Post not found")
    return post

def create_post(db: Session, post: PostCreate):
    return post_crud.create_post(db, post.title, post.content)

def update_post(db: Session, post_id: int, post: PostCreate):
    updated = post_crud.update_post(db, post_id, post.title, post.content)
    if not updated:
        raise Exception("Post not found")
    return updated

def delete_post(db: Session, post_id: int):
    deleted = post_crud.delete_post(db, post_id)
    if not deleted:
        raise Exception("Post not found")
    return deleted