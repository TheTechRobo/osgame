def hello():
    import random
    def sl(duration):
        import time
        time.sleep(duration)
    def printr(s):
        d = round(random.uniform(0, 1), 1) #source: https://stackoverflow.com/a/49614185/9654083
        print(s, end="\r")
        sl(d)
    printr("H")
    printr("He")
    printr("Hel")
    printr("Hell")
    printr("Hello")
    printr("Hello, ")
    printr("Hello, m")
    printr("Hello, my")
    printr("Hello, my n")
    printr("Hello, my na")
    printr("Hello, my nam")
    printr("Hello, my name ")
    printr("Hello, my name i")
    printr("Hello, my name is ")
    printr("Hello, my name is T")
    printr("Hello, my name is Th")
    printr("Hello, my name is The")
    printr("Hello, my name is TheT")
    printr("Hello, my name is TheTe")
    printr("Hello, my name is TheTec")
    print()
