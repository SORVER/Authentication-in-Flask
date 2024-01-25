from project import db ,create_app,models

# Create the Flask application
app = create_app()

# Use the application context to create the tables
with app.app_context():
    db.create_all()
