from matplotlib import pyplot as plt
import matplotlib.ticker as mticker  
import matplotlib
import numpy as np

if __name__ == "__main__":
  plt.rcParams['font.sans-serif'] = ['SimHei']

  plt.plot([0,75], [2,2], 'b')
  plt.plot([75,100,120],[20,0,20], 'b')
  plt.plot([120,195], [2,2], 'b')
  plt.axis([0,195,0,25])
  # plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter(x))
  # plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter(y))
  plt.xlabel('每日表标水平')
  plt.ylabel('利率')

  plt.show()