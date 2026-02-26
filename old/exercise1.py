def return_distincts(num1,num2,num3):

    val_list = [num1,num2,num3]

    total = num1 + num2 + num3

    if total > 15:
        max_val = max(val_list)
        return max_val
    elif total < 10:
        least_val = min(val_list)
        return least_val
    elif total >= 10 and total <=15:
        val_list.remove(max(val_list))
        val_list.remove(min(val_list))
        intermediate_val = val_list[0]
        return intermediate_val


print(return_distincts(6,3,8))

    