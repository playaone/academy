from app.extensions import db
from app.models.user import User


class UserRepository:
    def get_by_email(self, email: str) -> User | None:
        return db.session.execute(
            db.select(User).where(User.email == email)
        ).scalar_one_or_none()
