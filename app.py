from flask import Flask, request, jsonify
import os
from vedo import load, Plane

app = Flask(__name__)

# 輔助函數：檢查是否為float且在指定範圍內
def is_valid_float(value, min_val, max_val):
    try:
        float_value = float(value)
        if min_val <= float_value <= max_val:
            return True
    except ValueError:
        pass
    return False

@app.route('/cut_stl', methods=['POST'])
def cut_stl():
    data = request.json

    # 檢查參數是否存在
    required_params = ['cX', 'cY', 'cZ', 'vX', 'vY', 'vZ', 'input_path', 'output_path']
    for param in required_params:
        if param not in data:
            return jsonify(error="Missing parameter: {}".format(param)), 400

    cX = data['cX']
    cY = data['cY']
    cZ = data['cZ']
    vX = data['vX']
    vY = data['vY']
    vZ = data['vZ']
    input_path = data['input_path']
    output_path = data['output_path']

    # 檢查參數類型和範圍
    if not (is_valid_float(cX, -65535.0, 65535.0) and
            is_valid_float(cY, -65535.0, 65535.0) and
            is_valid_float(cZ, -65535.0, 65535.0)):
        return jsonify(error="Invalid center point values. Must be float and in range -65535.0 to 65535.0"), 400

    if not (is_valid_float(vX, -1.0, 1.0) and
            is_valid_float(vY, -1.0, 1.0) and
            is_valid_float(vZ, -1.0, 1.0)):
        return jsonify(error="Invalid vector values. Must be float and in range -1.0 to 1.0"), 400

    # 檢查目標stl檔案是否存在
    if not os.path.isfile(input_path):
        return jsonify(error="Input STL file does not exist"), 400

    # 檢查輸出路徑是否可用
    if os.path.exists(output_path):
        return jsonify(error="Output path is already occupied"), 400

    # 加載STL檔案並進行切割
    try:
        mesh = load(input_path)
        plane_origin = (float(cX), float(cY), float(cZ))
        plane_normal = (float(vX), float(vY), float(vZ))
        cut_mesh = mesh.cut_with_plane(origin=plane_origin, normal=plane_normal)
        cut_mesh.write(output_path)
    except Exception as e:
        return jsonify(error=str(e)), 500

    return jsonify(status="done"), 200

if __name__ == '__main__':
    app.run(debug=True)
