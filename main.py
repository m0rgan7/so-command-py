import win32net
users= win32.NetUserEnum(None, 0)
for users in users[0]:
    print(f"Nome:{users['name']}")
