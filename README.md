markdown
複製程式碼
# STL Cut Project

這是一個使用 Flask 和 Vedo 實現的 STL 檔案切割專案。該專案提供了一個 API，允許用戶上傳 STL 檔案並根據指定的切割平面參數進行切割。

## 目錄結構
```
STL_CUT/
├── app.py
├── cuted_heart1_stl.stl
├── heart1.stl
├── README.md
├── requirements.txt
└── send_cut_request.py
```


## 安裝

1. 克隆此存儲庫到本地：

```
git clone <repository-url>
cd STL_CUT
```
創建虛擬環境並激活它：
```
python -m venv venv
source venv/bin/activate  # 在Windows上使用`venv\Scripts\activate`
```
安裝所需的套件：

```
pip install -r requirements.txt
```

使用方法
啟動 Flask 伺服器
在終端中運行以下命令以啟動 Flask 伺服器：

```python app.py```

發送切割請求
在另一個終端窗口中運行 send_cut_request.py 以向本地運行的 API 發送切割請求：

```
python send_cut_request.py
```
## 傳入參數的意義

* cX, cY, cZ：切割平面的中心點資訊，要求為浮點數，範圍在 -65535.0 至 65535.0 之間。

* vX, vY, vZ：切割平面的法向量資訊，要求為浮點數，範圍在 -1.0 至 1.0 之間。

* input_path：目標 STL 檔案的路徑，要求為字串。

* output_path：切割完之後的 STL 檔案儲存路徑，要求為字串。

## 可能的錯誤代碼與解決方法
### 400 - Bad Request Missing parameter: {param}

說明：缺少必要的參數。
解決方法：確認請求中包含所有必要的參數：cX, cY, cZ, vX, vY, vZ, input_path, output_path。
### Invalid center point values. Must be float and in range -65535.0 to 65535.0


說明：中心點參數值無效。
解決方法：確認 cX, cY, cZ 是浮點數且範圍在 -65535.0 至 65535.0 之間。


### Invalid vector values. Must be float and in range -1.0 to 1.0

說明：法向量參數值無效。
解決方法：確認 vX, vY, vZ 是浮點數且範圍在 -1.0 至 1.0 之間。

### Input STL file does not exist

說明：目標 STL 檔案不存在。
解決方法：確認 input_path 指定的檔案存在於伺服器上。

### Output path is already occupied

說明：儲存檔案的路徑已被佔用。
解決方法：確認 output_path 指定的路徑沒有同名檔案存在。
500 - Internal Server Error

### SetOrigin argument 1: expected a sequence of 3 values, got Plane
說明：內部錯誤，通常是因為切割參數設置錯誤。
解決方法：檢查傳入的平面參數是否正確，並確保平面的位置和法向量參數正確傳遞。
示例請求
以下是向 API 發送請求的示例：

```json
{
    "cX": 0.0,
    "cY": 0.0,
    "cZ": -20.0,
    "vX": 0.0,
    "vY": 0.0,
    "vZ": -1.0,
    "input_path": "D:\\AWORKSPACE\\Github\\STL_cut\\heart1.stl",
    "output_path": "D:\\AWORKSPACE\\Github\\STL_cut\\cuted_heart1.stl"
}
```
聯絡方式
如有任何問題，請聯絡專案維護者。

go
複製程式碼

希望這個 `README.md` 文件能夠幫助你正確安裝、使用這個專案，並理解各個參數和錯誤代碼的意義。