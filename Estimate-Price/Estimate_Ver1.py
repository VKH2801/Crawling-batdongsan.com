# Sử dụng hồi quy tuyến tính để tính về định giá

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Dữ liệu bất động sản
data = {
    "price": ["17.063.750.000₫"],
    "size": ["67 sq m"],
    "attributes": ["Flat / Apartment"],
    "address": ["29B, Nguyen Dinh Chieu street, district 1"],
    "longitude": ["106.6991857"],
    "latitude": ["10.7870327"]
}

# Chuyển đổi dữ liệu thành DataFrame
df = pd.DataFrame(data)

# Xử lý và chuyển đổi dữ liệu
df["price"] = df["price"].str.replace("₫", "").str.replace(".", "").astype(float)
df["size"] = df["size"].str.extract(r"(\d+)").astype(float)
df["attributes"] = LabelEncoder().fit_transform(df["attributes"])

# Tạo các feature và target
X = df[["size", "attributes", "longitude", "latitude"]]
y = df["price"]

# Tạo mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X, y)

# Dự đoán giá bất động sản mới
new_data = {
    "size": [80],
    "attributes": ["Flat / Apartment"],
    "longitude": ["106.6991857"],
    "latitude": ["10.7870327"]
}
new_df = pd.DataFrame(new_data)
new_df["attributes"] = LabelEncoder().fit_transform(new_df["attributes"])
predicted_price = model.predict(new_df)

print("Predicted Price:", predicted_price)
