import pickle


def read_data():
    return pickle.load(open("data.pickle", "rb"))


def write_data(data):
    pickle.dump(data, open("data.pickle", "wb"))
