class PlayfairCipher:
    def __init__(self):
        pass
    
    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")  # Chuyển "J" thành "I" trong khóa
        key = key.upper()
        key_set = set()
        key_unique = ""
        
        # Loại bỏ ký tự trùng lặp trong key
        for char in key:
            if char not in key_set and char.isalpha():
                key_set.add(char)
                key_unique += char
        
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Không có J
        remaining_letters = [
            letter for letter in alphabet if letter not in key_set
        ]
        
        matrix_chars = key_unique + ''.join(remaining_letters)
        matrix_chars = matrix_chars[:25]  # Chỉ lấy 25 ký tự
        
        playfair_matrix = [list(matrix_chars[i:i+5]) for i in range(0, 25, 5)]
        return playfair_matrix
    
    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return None, None
    
    def playfair_encrypt(self, plain_text, matrix):
        # Chuyển "J" thành "I" và loại bỏ ký tự không phải chữ cái
        plain_text = plain_text.replace("J", "I").upper()
        plain_text = ''.join([c for c in plain_text if c.isalpha()])
        
        # Thêm X giữa các ký tự giống nhau
        processed_text = ""
        i = 0
        while i < len(plain_text):
            processed_text += plain_text[i]
            if i + 1 < len(plain_text) and plain_text[i] == plain_text[i + 1]:
                processed_text += "X"
            i += 1
        
        # Thêm X nếu độ dài lẻ
        if len(processed_text) % 2 == 1:
            processed_text += "X"
        
        encrypted_text = ""
        for i in range(0, len(processed_text), 2):
            char1, char2 = processed_text[i], processed_text[i + 1]
            row1, col1 = self.find_letter_coords(matrix, char1)
            row2, col2 = self.find_letter_coords(matrix, char2)
            
            if row1 == row2:  # Cùng hàng
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Cùng cột
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:  # Hình chữ nhật
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]
        
        return encrypted_text
    
    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        
        for i in range(0, len(cipher_text), 2):
            char1, char2 = cipher_text[i], cipher_text[i + 1]
            row1, col1 = self.find_letter_coords(matrix, char1)
            row2, col2 = self.find_letter_coords(matrix, char2)
            
            if row1 == row2:  # Cùng hàng
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Cùng cột
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:  # Hình chữ nhật
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]
        
        # Loại bỏ X thừa
        result = ""
        i = 0
        while i < len(decrypted_text):
            if i + 1 < len(decrypted_text) and decrypted_text[i + 1] == 'X':
                if i + 2 < len(decrypted_text) and decrypted_text[i] == decrypted_text[i + 2]:
                    result += decrypted_text[i]
                    i += 2  # Bỏ qua X
                else:
                    result += decrypted_text[i] + decrypted_text[i + 1]
                    i += 2
            else:
                result += decrypted_text[i]
                i += 1
        
        # Loại bỏ X cuối nếu có
        if result.endswith('X'):
            result = result[:-1]
        
        return result 