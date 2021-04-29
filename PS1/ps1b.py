
def dp_make_weight(egg_weights, target_weight, memo = {}):

    if target_weight in egg_weights:
        memo[target_weight] = 1
        return 1

    for  weight in range(1, target_weight +1):

        if weight in egg_weights:
            memo[weight] = 1
            continue

        qty_eggs = weight
        for egg in egg_weights:
            if egg > weight:
                continue
            if memo[weight - egg] + 1 < qty_eggs:
                qty_eggs = memo[weight - egg] + 1
            memo[weight] = qty_eggs
    return memo[target_weight]

if __name__ == '__main__':
    egg_weights = (1,5,10,25,27,39,45, 50, 67)
    n = 99
    print("Output:", dp_make_weight(egg_weights, n))
