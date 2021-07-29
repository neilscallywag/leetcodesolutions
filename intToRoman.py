def intToRoman(num):
    values = [1000, 900, 500, 400,
              100, 90, 50, 40,
              10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD",
               "C", "XC", "L", "XL",
               "X", "IX", "V", "IV",
               "I"]
    roman = ''
    i = 0
    while num > 0:
        k = num // values[i]
        print("num:",num , "i:", i,  "value:",values[i], "k:", k)
        for j in range(k):
            print(range(k))
            roman += symbols[i]
            print("for J =",j,roman)
            print("num-pre:",num)
            num -= values[i]
            print("num post:", num)
        i += 1
    return roman


print(intToRoman(223))
