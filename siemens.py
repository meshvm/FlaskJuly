# # string= "python programming"
# # str2=string[::-1]
# # print(str2)
# # new_dict ={}
# #
# # for i in string:
# #     new_dict[i]= string.count(i)
# #
# # print(new_dict)
# #
# #
# #
# # # class A:
# # #     MRO
#
# # def gen_function():
# #     for i in range(10):
# #         yield i*i
# #
# # for i in gen_function():
# #     print(i)
#
# # def mixer(fruit_juice):
# #     print("I am mixer")
# #     def blend():
# #         print("I am blender")
# #         fruit_juice()
# #     return blend
# #
# #
# # @mixer
# # def fruit_juice():
# #     print("juice is ready")
# # fruit_juice()
#
#
# def stove(dishes):
#     print("Turning ON the Stove !!")
#     def cooking():
#         print("Food gets ready in 15 min")
#         dishes()
#     return cooking
#
# @stove
# def prepare_food():
#     print("Ready to serve!!")
#
#
# @stove
# def prepare_lunch():
#     print("Lunch is ready")
#
#
# prepare_lunch()
# prepare_food()
#
# def grinder(item):
#     print("Make sure your grains are dry")
#     def atta():
#         print("Use me for Wheat")
#         item()
#         print("AATA piss gaya")
#     return atta
#
#
# @grinder
# def mill():
#     print("Yaha atta pisa jata h")
#
# print(mill())
#
#
# def decorator(todecorate):
#     def wrapper():
#         print("wrapped\t and ")
#         todecorate()
#     return wrapper()
#
# @decorator
# def todecorate():
#     print("decorated")
# print(todecorate)
# decorated = decorator(todecorate)
# print(decorated)
# def fun(n):
#     a=1
#     b=1
#     for i in range(2,n+1):
#         a,b = b,a+b
#     yield a
#
# fab = fun(3)
# s = iter(fab)
# print(next(s))


