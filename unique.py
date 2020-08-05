def unique_names(names1, names2):
    return None
if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    name = set(names1 + names2)
    name = sorted(name)
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia