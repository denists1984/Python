dicts = {'Denis T': ['Python'], 'Alex A': ['Unix'], 'George K': ['Perl', 'Ksh', 'Weblogic']}

def most_classes(dicts):
  big_num = 0
  skilled_teacher = ''
  for i in dicts:
    class_num = len(dicts[i])
    if (class_num > big_num):
      big_num = class_num
      skilled_teacher = i
  return skilled_teacher

def num_teachers(dicts):
    b = len(dicts.values())
    return b

def stats(dicts):
    stat = []
    for name, value in dicts.items():
        a = [name, len(value)]
        stat.append(a)
    return stat

def courses(dicts):
    cours = []
    for value in dicts.values():
        cours += value
    return cours
