def loss_or_profit(income, outcome):
    sum_in = 0
    sum_out = 0
    for i in income:
        sum_in += i
    for out in outcome:
        sum_out += out
    result = sum_in - sum_out
    if result == 0:
        return '=' + str(result)
    if result < 0:
        return str(result)
    if result > 0:
        return '+' + str(result)

