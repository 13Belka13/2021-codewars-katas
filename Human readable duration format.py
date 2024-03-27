def format_duration(seconds):
    s = {0: ['year', 'years'], 1:['day', 'days'], 2:['hour', 'hours'], 3:['minute', 'minutes'], 4:['second', 'seconds']}
    minutes = seconds // 60 % 60
    hours = seconds // 3600 % 24
    days = seconds // 86400 % 365
    years = seconds // 31104000
    seconds = seconds % 60
    z = [str(i) + ' ' + s[n][0] + ', ' if i == 1 else str(i) + ' ' + s[n][1] + ', ' for n, i in enumerate([years, days, hours, minutes, seconds]) if i > 0]
    if len(z) >= 1: z[-1] = z[-1][:-2]
    else: z = ['now']
    if len(z) >= 2: z[-2] = z[-2][:-2] + ' and '
    return ''.join(z)
print(format_duration(33243586))