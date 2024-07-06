# # rev_str = "Shivam Pandey"
# # new_str = rev_str[::-1]
# # print(new_str)
#
# # prime Numbers
# # def checkprime(n):
# #     count=0
# #     while n>0:
# #         for i in range(1,n+1):
# #             if n%i ==0:
# #                 count +=1
# #         return count
# #
# # def prime():
# #     n= int(input("Enter number to check prime:"))
# #     out= checkprime(n)
# #     if out ==2:
# #         print(True)
# #     else: print(False)
# #
# # prime()
#
# # rec = lambda x : x+3
# # while True:
# #     n=int(input("Enter Number"))
# #     print(rec(n))
#
# def file_handling():
#     fo = open("text.txt",'w')
#     for i in range(11):
#         fo.writel(str(i))
#     fo.close()
#
# def readfile():
#     fo = open('text.txt','r')
#     var = fo.read()
#     for itms in var:
#         print(itms)
#     fo.close
#
# file_handling()
# readfile()
#
#
#
#
def decorator(fun):
    print("I am Outer function decorator method")
    def inner():
        print("I am the main decorator function")
        return fun
    return inner()


@decorator
def todecorate():
    print("I have to decorate")

todecorate()
