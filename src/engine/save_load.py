import pickle

def save(state):
    with open("save.dat", "wb") as f:
        pickle.dump(state.__dict__, f)

def load(state):
    try:
        with open("save.dat", "rb") as f:
            data = pickle.load(f)
            state.__dict__.update(data)

    except:
        pass
    