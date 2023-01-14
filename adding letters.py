# 14. Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’


def addString(s: str):
  if s.endswith("ing"):
    return s + "ly"
  return s + "ing"
print(addString("test"))
print(addString("testing"))