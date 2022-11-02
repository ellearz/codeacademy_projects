#write a function that converts farenheit to celcius

def f_to_c(f_temp):
    c_temp = (f_temp - 32)* 5/9
    return c_temp

f100_in_celcius = f_to_c(100)
