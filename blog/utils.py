from datetime import date


def published_date(article_date):
    """return date as Today, or x days before or year-month-day"""
    delta = date.today() - article_date
    if delta.days == 0:
        return 'Today'
    elif delta.days == 1:
        return '{} day before'.format(delta.days)
    elif delta.days < 29:
        return '{} days before'.format(delta.days)
    else:
        return article_date.strftime("%B %-d, %Y")


def date_ymd(article_date):
    """return date as year-month-day"""
    return article_date.strftime("%Y-%m-%d")
