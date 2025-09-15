import re
import random
def main():
    sugest = "1234567890qwertyuiopasdfghjklzxcvbnm-=_+[´~]{)()}!@#$%¨&*'<>:,."
    passw = ""
    for i in range(0, 8, 1):
        passw = passw + sugest[random.randint(0, len(sugest) -1)]
    print(passw)
if __name__ == "__main__":
    main()