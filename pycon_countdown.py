from datetime import date

pycon_date = date(2018, 5, 10)
today = date.today()

days_till_pycon = (pycon_date - today).days


if (days_till_pycon != 0):
    print('Pycon is {} days away.'.format(str(days_till_pycon)))

else:
    print('Welcome to Pycon!')

