def month_year_start(date):
    """Get start date and return Month+Year"""
    short_date = date.strftime("%B %Y")
    return short_date


def year_start(date):
    """Get start date and return Year"""
    short_date = date.strftime("%Y")
    return short_date


def month_year_end(date):
    """Get end date and return Month+Year or Present instead of None"""
    if date is None:
        return "Present"
    else:
        short_date = date.strftime("%B %Y")
        return short_date


def year_end(date):
    """Get end date and return Year or Present instead of None"""
    if date is None:
        return "Present"
    else:
        short_date = date.strftime("%Y")
        return short_date
