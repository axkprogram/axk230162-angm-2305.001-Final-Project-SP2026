import pickle

def save_game(state, filename="save.dat"):
    with open(filename, "wb") as f:
        pickle.dump(state, f)