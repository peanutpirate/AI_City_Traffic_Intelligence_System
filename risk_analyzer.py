def calculate_risk(traffic, rain, hour):

    risk = traffic * 0.6 + rain * 0.2 + hour * 0.2

    if risk > 5000:
        return "HIGH RISK"
    elif risk > 3000:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"