# Furious Cocktail
# This assignment seems easy. Why don't we just sort in desceinding order and drink from the top down
# and see when we reach the buttom if all potions are in effect. We can do this by comparing the
# time_to_consume * <how many potions are left>, for all potions.

if __name__ == "__main__":
    amount_of_potions, time_to_consume = list(map(int, input().split()))
    potions = []
    for i in range(amount_of_potions):
        potions.append(int(input()))

    potions.sort(reverse=True)

    # Solution here:
    potions_chunked = 0
    all_in_effect = True
    for effect_time in potions:
        if(effect_time - time_to_consume*(amount_of_potions - potions_chunked - 1) <= 0):
            all_in_effect = False
            break
        potions_chunked += 1

    if(all_in_effect):
        print("YES")
    else:
        print("NO")
