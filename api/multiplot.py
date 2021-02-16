import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.pyplot import figure

t = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]
data1 = [327,456,509,497,596,573,661,741,809,717]
data2 = [29.8,30.1,30.5,30.6,31.3,31.7,32.6,33.1,32.7,32.8]
data3 = [27.8,28.1,28.5,28.6,29.3,29.7,30.6,31.1,30.7,30.8]


fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Years')
ax1.set_ylabel('Bedsheet tanglings', color=color)
ax1.plot(t, data1, color=color, marker="*")
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(300, 900)
ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.yaxis.set_minor_locator(AutoMinorLocator())


ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Cheese consumed (lbs)',loc='top', color=color)
ax2.plot(t, data2, color=color,marker="o")
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_xlim(1999, 2010)
ax2.set_ylim(29, 34)
ax2.xaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())

ax3 = ax1.twinx()
color = 'tab:green'
ax3.set_ylabel('Something Else',loc='center', color=color)
ax3.plot(t, data3, color=color,marker="o")
ax3.tick_params(axis='y', labelcolor='black')
ax3.set_xlim(1999, 2010)
ax3.set_ylim(29, 34)
ax3.xaxis.set_minor_locator(AutoMinorLocator())
ax3.yaxis.set_minor_locator(AutoMinorLocator())

ax4 = ax1.twinx()
color = 'orange'
ax4.set_ylabel('Something Else',loc='bottom', color=color)

#set_ylabel(self, ylabel, fontdict=None, labelpad=None, *, loc=None, **kwargs)

ax4.plot(t, data3, color=color,marker="o")
ax4.tick_params(axis='y', labelcolor='black')
ax4.set_xlim(1999, 2010)
ax4.set_ylim(29, 34)
ax4.xaxis.set_minor_locator(AutoMinorLocator())
ax4.yaxis.set_minor_locator(AutoMinorLocator())

plt.title("""Cheese consumption vs death by tangling themselves in their sheets""")
plt.subplots_adjust(left=None, bottom=None, right=None, top=0.4, wspace=None, hspace=None)
fig.tight_layout()
fig.set_size_inches(18.5, 10.5, forward=True)
plt.show()