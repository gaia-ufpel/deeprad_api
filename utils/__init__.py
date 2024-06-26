import os

HOST = os.getenv('HOST', 'localhost')
PORT = os.getenv('PORT', 5000)
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://localhost:5433/deeprad_api')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30