seasons = ["winter", "summer", "summer", "summer", "spring", "srping"]
def winter_is_coming(seasons):
    count = 0
    for season in seasons:
        if season != "winter":
            count += 1
    if count == 5:
        return True
    else:
        return False

print(winter_is_coming(seasons))