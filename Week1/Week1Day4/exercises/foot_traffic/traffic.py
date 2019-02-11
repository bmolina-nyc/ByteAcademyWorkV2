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

# counts the visits per room
def users_visits(users_coming):
    times = {}
    for list in users_coming:
        if list[1] not in times:
            times[list[1]] = 1
        else:
            times[list[1]] += 1
    return times

# works up the total time spent per room
def total_time_spent_per_room(users_coming, users_going):
   times = {} 
   sorted_users_coming = sorted(users_coming)
   sorted_users_going = sorted(users_going)
   i = 0
   while i < len(sorted_users_coming):
       if sorted_users_coming[i][1] not in times:
           times[sorted_users_coming[i][1]] = ( int(sorted_users_going[i][3]) - int(sorted_users_coming[i][3]) )
       else: 
            times[sorted_users_coming[i][1]] += ( int(sorted_users_going[i][3]) - int(sorted_users_coming[i][3]) )
       i += 1   
   return times

time_spent_per_room = total_time_spent_per_room(users_coming, users_going)
total_user_vists = users_visits(users_coming)

# averages
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
    final_copy = []
    while i < len(output):
        final_copy.append(f'Room {output[i][0]}, {output[i][1]} minute average visit, {output[i][2]} visitors(s) totals')
        i += 1
    return final_copy

final_traffic_output = final_output(output)

final_output = open("finaloutput.txt", "w")
for line in final_traffic_output:
    final_output.write(line)
    final_output.write('\n')
final_output.close()



