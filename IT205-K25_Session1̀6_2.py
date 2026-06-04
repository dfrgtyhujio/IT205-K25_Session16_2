# - Phép gán "=" chỉ tạo tham chiếu (nhãn mới), trỏ chung một vùng nhớ với list gốc.
#   Vì vậy, khi dùng .append() thì cả hai biến cùng thay đổi.
# - Hai cách tạo bản sao (copy) độc lập:
#   + Cách 1: old_list.copy()
#   + Cách 2: old_list[:]
# - Hàm .replace() không có tác dụng vì String là bất biến (Immutable), không tự sửa đổi.
# - Cú pháp sửa lại: new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")


yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

def update_prescription(old_prescription):
    new_prescription = old_prescription.copy()
    
    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")
    
    new_prescription.append("Oresol")
    return new_prescription
    
today_prescription = update_prescription(yesterday_prescription)

print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)
