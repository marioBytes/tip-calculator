import math

#get subtotal
subtotal = float(input('What is the subtotal? $'))

#get gratuity
gratuity = float(input('What is the percentage of gratuity? '))

new_total = float(gratuity / 100 * subtotal + subtotal)

#get tip
tip = float(input('What is the tip percentage you would like to leave? '))

total = float(tip / 100 * new_total)

print('Your tip amount is: $', round(total, 2))
