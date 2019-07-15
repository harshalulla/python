def ask_ok(prompt, retries=2, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

print("Nummber 1\tThe Larch\nNumber 2\tThe Horse Chestnut")
ask_ok('OK to overwrite the file?', 5)