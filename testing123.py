
# test = {
#     0 : 'first value in my dict',
#     1 : 'second thing in the dictionary',
#     2 : 'third thing'
# }

# print(test[1])

# def keys_makr(some_crazy_thing):
#     list_of_keys = []
#     for i in some_crazy_thing.keys():
#         list_of_keys.append(i)
#     return list_of_keys

# key_list = keys_makr(test)

# print(test[0])

# # print(test.keys())

# # keys = test.keys()

# # print(test)


# print(test.items())
# print(test.keys())
# print(test.values())
# print("------")
# for key, val in enumerate(test):
#     if key == 1:
#         del test[key]
#     print(key, val)

service_tickets = {
    1 : {"Customer": "Alice", "Issue": "Login problem", "Status": True},
    2 : {"Customer": "Bob", "Issue": "Payment issue", "Status": False}
}

def update_ticket():
    while True:
        try: 
            ans = int(input("which ticket id would you like to update? "))
            if ans in service_tickets.keys():
                if service_tickets[ans]['Status']:
                    service_tickets[ans]['Status'] = False
                    print(service_tickets[ans])
                    break
                elif not service_tickets[ans]['Status']:
                    service_tickets[ans]['Status'] = True
                    print(service_tickets[ans])
                    break
            else:
                print("Enter an existing ticket ID")
        except:
            print("enter numerical values only")
            continue

update_ticket()
#closing a ticket
# service_tickets[1]['Open'] = False

# print(service_tickets[1]['Open'])
# print(service_tickets)

# service_tickets[1]['Status'] = "Closed"
# print(service_tickets)

# if service_tickets[1]['Status'] == 'Closed':
#     service_tickets[1]['Status'] = 'Open'

# print(service_tickets)
