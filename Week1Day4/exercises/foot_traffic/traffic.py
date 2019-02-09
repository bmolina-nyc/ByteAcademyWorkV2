import operator
'''
['0', '5', 'I', '330']
visitors unique id, room number, I for in or O for out of room, 
minute they left room (1440 mins in a day)
'''
def print_file(filename):
    printed_text = []
    with open(filename) as file_object:
        text = file_object.readlines()
    for line in text:
        printed_text.append(line.split())
    return printed_text

# formatted dataset text file
dataset = print_file('traffic.txt')


def users_in(dataset):
    users_in = []
    for item in dataset:
        if item[2] == 'I':
            users_in.append(item)
    return users_in

def users_out(dataset):
    users_out = []
    for item in dataset:
        if item[2] == 'O':
            users_out.append(item)
    return users_out

users_coming, users_going = users_in(dataset), users_out(dataset)

def users_visits(users_coming):
    times = {}
    for list in users_coming:
        if list[1] not in times:
            times[list[1]] = 1
        else:
            times[list[1]] += 1
    return times

def total_time_spent_per_room(users_coming, users_going):
   sorted_users_coming = sorted(users_coming)
   sorted_users_going = sorted(users_going)
   times = {} 
   i = 0
   while i < len(sorted_users_coming):
       times[sorted_users_coming[i][1]] = ( int(sorted_users_going[i][3]) - int(sorted_users_coming[i][3]) )
       i += 1   
   return times

time_spent_per_room = total_time_spent_per_room(users_coming, users_going)
total_user_vists = users_visits(users_coming)

def averages_visits_per_room(time_spent_per_room, total_user_vists):
    times = []
    time_spent_per_room = time_spent_per_room
    total_user_vists = total_user_vists
    room_keys = list(dict.keys(time_spent_per_room))

    for key in room_keys:
        # output is  [ 'room number' ,  total visitor time in room,  total visits ]
        times.append( [ key,  (time_spent_per_room[key] // total_user_vists[key]) , total_user_vists[key] ] )
    return times
   
output = averages_visits_per_room(time_spent_per_room, total_user_vists)

def final_output(output):
    i = 0 
    while i < len(output):
        print(f'Room {output[i][0]}, {output[i][1]} minute average visit, {output[i][2]} visitors(s) totals')
        i += 1



print(final_output(output))



