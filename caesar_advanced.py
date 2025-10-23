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
        print("\n" + "-"*50)
        print("РЕЖИМ ШИФРОВАНИЯ/ДЕШИФРОВАНИЯ")
        print("-"*50)
        
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


class CaesarBruteforce:
    def __init__(self, cipher):
        self.cipher = cipher
    
    def brute_force(self, encrypted_text: str, language: str, max_results: int = 10):
        results = []
        
        if language == 'русский':
            max_shift = 32
        else:
            max_shift = 26
        
        print(f"\nНачинается перебор {max_shift} возможных сдвигов...")
        
        for shift in range(1, max_shift):
            try:
                decrypted = self.cipher.process_text(
                    encrypted_text, shift, language, 'дешифровать'
                )
                results.append({
                    'shift': shift,
                    'text': decrypted,
                    'score': self._calculate_readability_score(decrypted, language)
                })
            except Exception as e:
                continue
        
        results.sort(key=lambda x: x['score'], reverse=True)
        
        print(f"Найдено {len(results)} вариантов. Топ-{max_results}:\n")
        
        for i, result in enumerate(results[:max_results], 1):
            print(f"#{i} Сдвиг: {result['shift']} | Читаемость: {result['score']:.1f}%")
            print("Результат: " + result['text'])
            print("-" * 40 + "\n")
        
        return results[:max_results]
    
    def _calculate_readability_score(self, text: str, language: str) -> float:
        common_letters_ru = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъ'
        common_letters_en = 'etaoinshrdlcumwfgypbvkjxqz'
        
        common_letters = common_letters_ru if language == 'русский' else common_letters_en
        text_lower = text.lower()
        
        if len(text_lower) == 0:
            return 0.0
        
        common_count = sum(1 for char in text_lower if char in common_letters[:10])
        score = (common_count / len(text_lower)) * 100
        
        return min(score, 100.0)
    
    def interactive_bruteforce(self):
        print("\n" + "-"*50)
        print("РЕЖИМ ВЗЛОМА ШИФРА ЦЕЗАРЯ")
        print("-"*50)
        
        while True:
            language = input('Язык текста (русский/английский): ').lower()
            if language in ['русский', 'английский']:
                break
            print('Ошибка: введите "русский" или "английский"')
        
        while True:
            encrypted_text = input('Зашифрованный текст: ').strip()
            if encrypted_text and not encrypted_text.isspace():
                break
            print('Ошибка: текст не может быть пустым')
        
        try:
            max_input = input('Сколько вариантов показать (по умолчанию 10): ').strip()
            max_results = int(max_input) if max_input else 10
        except ValueError:
            max_results = 10
            print('Использую значение по умолчанию: 10')
        
        self.brute_force(encrypted_text, language, max_results)


def main():
    cipher = CaesarCipher()
    bruteforcer = CaesarBruteforce(cipher)
    
    while True:
        print("\n" + "-"*50)
        print("ШИФР ЦЕЗАРЯ")
        print("-"*50)
        print("1. Шифрование/дешифрование")
        print("2. Взлом шифра (brute force)")
        print("3. Выход")
        
        choice = input("\nВыберите режим (1-3): ").strip()
        
        if choice == '1':
            cipher.interactive_mode()
        elif choice == '2':
            bruteforcer.interactive_bruteforce()
        elif choice == '3':
            print("\nКонец!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
