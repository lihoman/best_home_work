import os


class FindingCoincidence:

    def __init__(self, user_phrase, path):
        self.user_phrase = user_phrase
        self.path = path

    def find_coincidence(self):
        os.chdir(self.path)
        list_of_books = []
        for root, dirs, files in os.walk(self.path):
            for i in files:
                self.open_files(i, list_of_books)
        return list_of_books

    def open_files(self, file_name, list_name):
        try:
            with open(file_name) as f:
                if self.user_phrase.lower() in f.read().lower():
                    list_name.append(file_name)
        except UnicodeDecodeError:
            with open(file_name, encoding='utf-8') as f:
                if self.user_phrase.lower() in f.read().lower():
                    list_name.append(file_name)
        return list_name

    def answer_to_user(self):
        path = self.find_coincidence()
        if path:
            return path
        else:
            return 'There are no books containing your phrase'
