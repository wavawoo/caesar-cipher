class CaesarCipher:
    UPPER_ENG_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWER_ENG_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    UPPER_RUS_ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    LOWER_RUS_ALPHABET = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    
    def __init__(self):
        self.supported_languages = {'русский', 'английский'}
        self.supported_operations = {'шифровать', 'дешифровать'}
    
    def _get_alphabet_info(self, language: str) -> tuple:
        if language == 'русский':
            return (self.LOWER_RUS_ALPHABET, self.UPPER_RUS_ALPHABET, 32)
        elif language == 'английский':
            return (self.LOWER_ENG_ALPHABET, self.UPPER_ENG_ALPHABET, 26)
    
    def _validate_input(self, text: str, step: int, language: str, operation: str) -> None:
        if not text or text.isspace():
            raise ValueError("Текст не может быть пустым")
        
        if not isinstance(step, int) or step < 0:
            raise ValueError("Шаг должен быть неотрицательным целым числом")
        
        if language not in self.supported_languages:
            raise ValueError(f"Поддерживаемые языки: {', '.join(self.supported_languages)}")
        
        if operation not in self.supported_operations:
            raise ValueError(f"Поддерживаемые операции: {', '.join(self.supported_operations)}")
    
    def process_text(self, text: str, step: int, language: str, operation: str) -> str:
        self._validate_input(text, step, language, operation)
        
        lower_alphabet, upper_alphabet, alpha_len = self._get_alphabet_info(language)
        result = []
        
        shift = step if operation == 'шифровать' else -step
        
        for char in text:
            if char in upper_alphabet:
                place = upper_alphabet.index(char)
                new_index = (place + shift) % alpha_len
                result.append(upper_alphabet[new_index])
            elif char in lower_alphabet:
                place = lower_alphabet.index(char)
                new_index = (place + shift) % alpha_len
                result.append(lower_alphabet[new_index])
            else:
                result.append(char)
        
        return ''.join(result)
    
    def interactive_mode(self):
        print("Шифр Цезаря\n")
        
        while True:
            operation = input('Что сделать: шифровать или дешифровать? ').lower()
            if operation in self.supported_operations:
                break
            print('Ошибка: введите "шифровать" или "дешифровать"')
        
        while True:
            language = input('Язык текста: русский или английский? ').lower()
            if language in self.supported_languages:
                break
            print('Ошибка: введите "русский" или "английский"')
        
        while True:
            step_input = input('Шаг сдвига (число): ')
            if step_input.isdigit():
                step = int(step_input)
                break
            print('Ошибка: введите целое число')
        
        while True:
            text = input('Введите текст: ').strip()
            if text and not text.isspace():
                break
            print('Ошибка: текст не может быть пустым')
        
        try:
            result = self.process_text(text, step, language, operation)
            print(f"\nРезультат: {result}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


def main():
    cipher = CaesarCipher()
    cipher.interactive_mode()


if __name__ == "__main__":
    main()
