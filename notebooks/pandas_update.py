time = []

for ts in air_quality['Time']:
    if ts.split()[1] == '24:00:00':
        ts = ts.replace('24:00:00', '00:00:00')
        date = pd.to_datetime(ts, format='%Y-%m-%d %H:%M:%S') + datetime.timedelta(days=1)
    else:
        date = pd.to_datetime(ts, format='%Y-%m-%d %H:%M:%S')
    time.append(date)
    
air_quality['Time'] = time