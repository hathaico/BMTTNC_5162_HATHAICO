class TranspositionCipher:
    def __init__(self):
        pass
    
    def encrypt(self, text, key):
        encrypted_text = ""
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text
    
    def decrypt(self, text, key):
        # Tính số hàng cần thiết
        num_rows = len(text) // key
        if len(text) % key != 0:
            num_rows += 1
        
        # Tính số ký tự trong mỗi cột
        num_chars_per_col = len(text) // key
        extra_chars = len(text) % key
        
        # Tạo ma trận để lưu kết quả
        decrypted_text = [''] * len(text)
        
        # Điền dữ liệu vào ma trận theo cột
        index = 0
        for col in range(key):
            # Số ký tự trong cột này
            chars_in_this_col = num_chars_per_col
            if col < extra_chars:
                chars_in_this_col += 1
            
            # Điền ký tự vào các vị trí tương ứng
            for row in range(chars_in_this_col):
                position = row * key + col
                if position < len(text):
                    decrypted_text[position] = text[index]
                    index += 1
        
        return ''.join(decrypted_text) 