def get_choice_for_table():
    stats = [0, 0, 0]
    with open("./data/choice.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            yourself, online, tutor, src = line.split(";")
            stats += [yourself, online, tutor]
    return stats

def write_choice(yourself, online, tutor):
    new_choice_line = f"{1 if yourself == 'on' else 0};{1 if online == 'on' else 0};{1 if tutor == 'on' else 0};user"
    with open("./data/choice.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]
    terms_sorted = old_terms + [new_choice_line]
    terms_sorted.sort()
    new_terms = [title] + terms_sorted
    with open("./data/choice.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))

def get_choice_stats():
    yourself_score = 0
    online_score = 0
    tutor_score = 0
    user_choice = 0
    db_choice = 0
    with open("./data/choice.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            yourself, online, tutor, src = line.split(";")
            if int(yourself):
                yourself_score += 1
            if int(online):
                online_score += 1
            if int(tutor):
                tutor_score += 1
            if "user" in src:
                user_choice += 1
            elif "db" in src:
                db_choice += 1
    stats = {
        "yourself": yourself_score,
        "online": online_score,
        "tutor": tutor_score,
        "db_added": db_choice, 
        "user_added": user_choice
    }
    return stats
