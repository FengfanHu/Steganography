#RS Analyse

#Mask
M = (0,1,1,0)
M_1 = (0,-1,-1,0)

def f1(value):
  if value%2 == 0:
    value += 1
  else:
    value -= 1
  return value

def f_1(value):
  if value%2 == 0:
    value -= 1
  else:
    value += 1
  return value

if __name__ == "__main__":
  pass
  # values = []
  # for row in range(rows):
  #   for column in range(columns):
  #     value = img1.item(row, column)
  #     values.append(value)

  # valuesf1 = []
  # for v in values:
  #   value = f1(v)
  #   valuesf1.append(value)

  # valuesf_1 = []
  # for v in values:
  #   value = f_1(v)
  #   valuesf_1.append(value)

  # sub = []
  # for i in range(len(values)):
  #   value = valuesf1[i] - valuesf_1[i]
  #   sub.append(value)
