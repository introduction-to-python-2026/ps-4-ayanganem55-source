def split_before_each_uppercases(formula):

    parts = []
    current_part = ""

    for ch in formula:
        if ch.isupper() and current_part:

            parts.append(current_part)
            current_part = ch
        else:
            current_part += ch


        if current_part:
            parts.append(current_part)

    return parts



def split_at_first_digit(formula):
    digit_location = 1

    for ch in formula[1:]:
        if ch.isdigit():
            break   
        digit_location += 1


    if digit_location == len(formula):
        return formula, 1
        
    prefix = formula[:digit_location]
    number = int(formula[digit_location:])
    return prefix, number

