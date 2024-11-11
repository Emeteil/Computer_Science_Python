from random import sample

input_folder = "input"
filename  = "file9.txt"

def password_generation(
        min_len_word: int = 3,
        range_out_len: (int, int) = (8, 10) # type: ignore
    ) -> str:
    with open(f"{input_folder}/{filename}", 'r', encoding='utf-8') as f:
        text = f.read()
        
    words = [
        word.capitalize()
        for word in text.split()
        if min_len_word <= len(word) <= (range_out_len[1] - min_len_word) 
    ]
    
    while True:
        password: str = ''.join(sample(words, 2))
        if range_out_len[0] <= len(password) <= range_out_len[1]: break
    
    return password

def main():
    password: str = password_generation(3, (8, 10))
    print(password)

if __name__ == "__main__":
    main()