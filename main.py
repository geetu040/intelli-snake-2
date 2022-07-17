from fastapi import FastAPI
import json, utility

app = FastAPI()

"""
# USED ON LOCAL HOST
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://192.168.1.108:3000",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""

@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/intelli-snake-2/map-{info}")
def intelliSnake2_map(info:str):
	returned_info = utility.load_map( json.loads(info) )
	return json.dumps(returned_info)

@app.get("/intelli-snake-2/automate-{info}")
def automate(info:str):
	predicted_dirs = utility.automate( json.loads(info) )
	return predicted_dirs

@app.get("/intelli-snake-2/automate_faster-{info}")
def automate_faster(info:str):
	returned_infos = utility.automate_faster( json.loads(info) )
	return json.dumps(returned_infos)

@app.get("/intelli-snake-2/write-{content}")
def write(content:str):
	with open("latest_dataset.txt", "a") as f:
		f.write(content)
	return "nothing"