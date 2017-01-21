MONTH_NAMES = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

def month_to_name(month):
    if month < 1 or month > 12:
        raise IndexError("Month must be between 1 and 12!: %d" % month)

    return MONTH_NAMES[month-1]


