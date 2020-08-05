# def konju(*a):
#     print(a)
#     for i in a:
#         print(i*2)
# konju(2, 4, 6, 8)



# def name(*kids):
#     print(kids)
#     for i in kids:
#         print(i.lower())
# name("JOY", "KEMI", "JOHN")



# def name(*kids):
#     print(kids)
#     for i in kids:
#         for x in i:
#             print(x.lower())
# name("JOY", "KEMI", "JOHN")



# def name(*kids):
#     print(kids)
#     for i in kids:
#         for x in i:
#             print(x.swapcase())
# name("Joy", "KeMi", "JoHn")



# def key_word_func(a,b,c):
#     print("a =", a,"b =", b, "c =", c)

# key_word_func("b", "c", "a")

#this is a positional argument. but if you want to print normal...


# def key_word_func(a,b,c):
#     print("a =", a,"b =", b, "c =", c)

# key_word_func(b ="b", c = "c", a = "a")




# variable keyword arguments (this is in dictionary format)

# def students(**data):
#     print(data)

# students(ade=23, bolu=12, shade=54, sean=50)


# def students(**data):
#     print(data.keys())

# students(ade=23, bolu=12, shade=54, sean=50)


# def students(**data):
#     print(data.values())

# students(ade=23, bolu=12, shade=54, sean=50)


# class exercise.


# def goods(**items):
#     for key in items:
#         print(key, ":", items[key])

#     prices = sum(items.values())
#     print("Total :", prices)

# goods(rice = 200, beans = 120, gari = 150, soya = 300, corn = 500)





def sort_values(*scattered_list, should_be_ascending = True):

    scattered_list = list(scattered_list)

    for i in range(len(scattered_list)):
        for i in range(len(scattered_list)-1):
            if scattered_list[i] > scattered_list[i+1]:
                scattered_list[i], scattered_list[i+1] = scattered_list[i+1], scattered_list[i]

if should_bea_ascending:
    print(scattered_list)
else:
    print(scattered_list[::-1])