def get_philosophers_for_table():
    terms = []
    with open("./data/p hilosophers.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            name, years, bio = line.split(";")
            terms.append([cnt, name, years, bio])
            cnt += 1
    return terms