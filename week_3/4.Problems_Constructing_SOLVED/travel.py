def travel_cost(travels):
    total_sum = 0
    for travel in travels:
        if travel >= 23:
            total_sum += 23
        else:
            total_sum += travel * 1

    if total_sum >= 50:
        return 50
    elif total_sum < 50 and total_sum >= 23:
        return "Get a card"
    elif total_sum < 23:
        return "You can use tickets"
print(travel_cost([28, 5, 23]))
