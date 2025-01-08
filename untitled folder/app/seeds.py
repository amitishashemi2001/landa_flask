from app.extensions import db
from app.models import User
from app.models import Permission

def seed_users():
    admin = User(username="admin", password="admin123", is_admin=True)
    user = User(username="user", password="user123")

    db.session.add(admin)
    db.session.add(user)
    db.session.commit()


def seed_permissions():
    permissions = ["can_edit_name", "can_edit_id", "can_view_users"]

    for perm in permissions:
        if not Permission.query.filter_by(name=perm).first():
            new_perm = Permission(name=perm)
            db.session.add(new_perm)

    db.session.commit()
    print("Permissions seeded successfully!")
