from app.seeds import seed_permissions

def register_commands(app):
    @app.cli.command("seed_permissions")
    def seed():
        """Seed the database with permissions."""
        with app.app_context():
            seed_permissions()
