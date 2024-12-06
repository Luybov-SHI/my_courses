class WordsFinder:
    def __init__(self, data_text):
        data_text = str (data_text)
        self.file_names = 'test_file.txt'
        file = open (self.file_names, 'w', encoding='utf-8')
        file.write (data_text)
        file.close ()

    def get_all_words(self):
        with open (self.file_names, encoding='utf-8') as file:
            word = file.read ()
            puncs = ',', '.', '=', '!', '?', ';', ':', ' - '
            for punc in puncs:
                if punc in word:
                    word = word.replace (punc, ' ')
                    continue
            word = word.split ()
        all_words = {}
        all_words[f'test_file.txt'] = word
        return all_words

    def find(self, word):
        for key, value in self.get_all_words ().items ():
            finds = {}
            if word.lower () in value:
                finds[key] = value.index (word.lower ()) + 1
                return finds

    def count(self, word):
        counts = {}
        for value, key in self.get_all_words ().items ():
            words = key.count (word.lower ())
            counts[value] = words
            return counts


data_text = ("It's a text for task Найти везде.\n"
             " Используйте его для самопроверки.\n"
             " Успехов в решении задачи!\ntext,text,text")

finder2 = WordsFinder (data_text)
print (finder2.get_all_words ())
print (finder2.find ('TEXT'))
print (finder2.count ('teXT'))