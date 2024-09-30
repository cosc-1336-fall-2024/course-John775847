

def get_options_ratio(option, total):
    ratio = option/total
    return ratio

def get_faculty_rating(ratio):
    if (ratio > 1 or ratio < 0):
        return "error"
    elif (ratio == 1):
        return "Perfect"
    elif (ratio > 0.9):
        return "Excellent"
    elif (ratio > 0.8):
        return "Very Good"
    elif (ratio > 0.7):
        return "Good"
    elif (ratio > 0.6):
        return "Needs Improvement"
    else:
        return "Unacceptable"
    return "error"
