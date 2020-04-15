import pickle


class DatabaseConnector:

    def __init__(self, file_path):
        self.path = file_path

    def save(self, obj):
        print('(SAVE)', self.path, obj)
        fj = open(self.path, 'wb')
        pickle.dump(obj, fj)
        fj.close()

    def load(self):
        fj = open(self.path, 'rb')
        data = pickle.load(fj)
        fj.close()
        print('(LOAD)', self.path, data)
        return data
