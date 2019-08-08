import twint

#Enter Twitter Handler


def user_input():
    handler = input("Enter a twitter handler: ")
    return handler


def handlers(handler):
    handlers = []
    handlers.append(handler)


print(user_input())
print(handlers(user_input())