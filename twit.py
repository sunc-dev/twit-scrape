import twint
#Enter Twitter Handler


def user_input():
    handler = input("Enter a twitter handler: ")
    start = input("Enter a date to start the search: ")
    end = input("Enter a date to end the search: ")
    return handler, start, end


def handlers(handler):
    handlers = []
    handlers.append(handler)
    return handler


c = twint.Config()
c.Username = user_input()
print(handlers(c.Username))
