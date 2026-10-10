test_string = '1h 45m,360s,25m,30m 120s,2h 60s'
sum_minutes = 0

arr_values = test_string.split(',')
for i in arr_values:
    arr_items = i.split(' ')
    for j in arr_items:
        if 'h' in j:
            sum_minutes += int(j.replace('h', '')) * 60
        elif 'm' in j:
            sum_minutes += int(j.replace('m', ''))
        elif 's' in j:
            sum_minutes += int(j.replace('s', '')) // 60
        else:
            print('Unknown symbols')
            continue

print(sum_minutes)
