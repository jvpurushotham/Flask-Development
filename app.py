from flask import Flask
from app.routes.department import department_bp

from app import create_app

app = create_app()

app.register_blueprint(department_bp)

if __name__ == "__main__":
    app.run(debug=True)