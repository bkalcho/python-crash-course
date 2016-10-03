guests = ['gvozden', 'mirko', 'milovan', 'marija']
message1 = 'I am inviting you '
message2 = ' as a guest'

print('My dinner table is late, so I can invite only two people on the dinner')
cancel_guest = guests.pop()
print('Sorry I can not invite you on dinner ' + cancel_guest)
cancel_guest = guests.pop()
print('Sorry I can not invite you on dinner ' + cancel_guest)

print(message1 + guests[0] + message2)
print(message1 + guests[1] + message2)

del guests[1]
del guests[0]
print(guests)