guests = ['gvozden', 'mirko', 'milovan', 'marija']
message1 = 'I am inviting you '
message2 = ' as a guest'

print('I have just found a bigger table')
guests.insert(0, 'zoran')
guests.insert(3, 'stefan')
guests.append('ljubinka')

print(message1 + guests[0] + message2)
print(message1 + guests[1] + message2)
print(message1 + guests[2] + message2)
print(message1 + guests[3] + message2)
print(message1 + guests[4] + message2)
print(message1 + guests[5] + message2)
print(message1 + guests[6] + message2)