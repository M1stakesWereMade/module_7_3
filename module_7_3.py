import string

class WordsFinder:
    def __init__(self, *file_names):
        """
        Конструктор, принимает названия файлов и сохраняет их в атрибут file_names.
        """
        self.file_names = list(file_names)

    def get_all_words(self):
        """
        Читает слова из каждого файла, возвращая словарь вида:
        {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4']}
        """
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(punct, ' ')
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        """
        Ищет слово в каждом файле, возвращая словарь:
        {'file1.txt': позиция, ...}
        Если слово не найдено, позиция равна -1.
        """
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            try:
                position = words.index(word) + 1
            except ValueError:
                position = -1
            result[name] = position
        return result

    def count(self, word):
        """
        Считает количество вхождений слова в каждом файле, возвращая словарь:
        {'file1.txt': количество, ...}
        """
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            result[name] = words.count(word)
        return result

finder = WordsFinder('test_file.txt')

print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))
