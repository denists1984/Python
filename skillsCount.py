dicts = {'Denis T': ['Python'], 'Alex A': ['Unix'], 'George K': ['Perl', 'Ksh', 'Weblogic'], 'Sami B': ['Unix', 'SysAdmin', 'Perl', 'Ksh', 'Weblogic']}

def most_classes(dicts):
    a = len(dicts.values())
    for i in dicts:
        if len(dicts[i]) >= a:
            print len(dicts[i])
            value = i
    return value
