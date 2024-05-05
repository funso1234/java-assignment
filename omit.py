def both_ends(s):
  if len(s) <= 2:
    return ""
  else:
    return s[0] + s[1] + s[len(s)-2] + s[len(s-1)]
  return