def normalize_name(name):
    for c in name:
        if c in ['!', '@', '#', '$', '%', '^', '&', '*']:
            name = name.replace(c, "")
    normal_name = name.strip()
    normal_name = normal_name.lower()
    normal_name = normal_name.replace(" ", "_")
    return normal_name

    
def cumsum(xs):
    sums = [xs[0]]
    for x in xs[1:]:
        sums.append(sums[-1] + x)
    return sums