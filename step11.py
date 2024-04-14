def get_date(date_dict):
    return str(date_dict.get('year')) + '-' + str(date_dict.get('month')) + '-' + str(date_dict.get('day'))


date_dict = {'year': 2024, 'month': 4, 'day': 14}
print(get_date(date_dict))
