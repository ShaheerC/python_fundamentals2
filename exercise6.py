def to_c(frn):
    cel = (frn - 32) * 5/9
    return str(cel)

print ("Hello, please enter your temperature in Farenheit.")
frn = int(input())

print('Your current temperature in celsius is {}'.format(to_c(frn)))