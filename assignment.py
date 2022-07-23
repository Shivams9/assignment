l = [
    {"Dg set": "Diesel generator"},
    {"Organization": "Organisation"},
    {"Group": "Organisation"},
    {"Orange": "Kinnu"},
    {"Orange": "narangi"}
]
groups = []
for each in l:
    # print(each)
    for key, value in each.items():
        # print(key, value)
        added = False
        for group in groups:
            if key in group or value in group:
                group.add(key)
                group.add(value)
                added = True
                break
        if not added:
            group = set()
            group.add(key)
            group.add(value)
            groups.append(group)
print(groups)
