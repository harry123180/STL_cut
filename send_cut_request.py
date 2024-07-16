import requests
import json

# 定義API端點和請求數據
api_url = "http://127.0.0.1:5000/cut_stl"
data = {
    "cX": 0.0,
    "cY": 0.0,
    "cZ": -20.0,
    "vX": 0.0,
    "vY": 0.0,
    "vZ": -1.0,
    "input_path": "D:\\AWORKSPACE\\Github\\STL_cut\\heart1.stl",
    "output_path": "D:\\AWORKSPACE\\Github\\STL_cut\\cuted_heart1_stl.stl"
}

# 發送POST請求到API
response = requests.post(api_url, json=data)

# 檢查回應狀態
if response.status_code == 200:
    print("Request was successful:", response.json())
else:
    print("Request failed with status code:", response.status_code)
    print("Error message:", response.json())

