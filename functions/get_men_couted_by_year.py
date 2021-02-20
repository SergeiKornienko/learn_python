from collections import Counter
from datetime import date


def get_men_counted_by_year(users):
    def is_man(user):
        return user['gender'] == 'male'
    men_users = list(filter(is_man, users))
    years = Counter()
    for user in men_users:
        years[date.fromisoformat(user['birthday']).year] += 1
    return dict(years)
