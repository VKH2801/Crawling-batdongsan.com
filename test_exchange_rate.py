from forex_python.converter import CurrencyRates
from datetime import datetime, timedelta

# Khởi tạo đối tượng CurrencyRates
c = CurrencyRates()

# Lấy tỉ giá hối đoái từ USD sang VND tại thời điểm 1 tháng trước
date = datetime.now() - timedelta(days=60)
exchange_rate = c.get_rate('USD', 'VND', date)

# In kết quả
print('Tỉ giá hối đoái từ USD sang VND là: ', exchange_rate)
