import matplotlib.pyplot as plt
limit = 3
fig, axes = plt.subplots(nrows=limit, ncols=limit, sharex=True, sharey=True, )

for i in range(limit):
    for j in range(limit):
        ax = axes[i, j]
        ax.set_xbound(lower=-2, upper=2)
        ax.set_ybound(lower=-2, upper=2)
        ax.grid()
        ax.set_aspect('equal', adjustable='box')

# show
fig = plt.gcf()
fig.canvas.manager.window.showMaximized()
fig.canvas.set_window_title('Test')
plt.tight_layout() # TODO: comment this line to see the difference if tight layout is not specified

# TODO: uncomment the following block to see that nothing happens if tight layout and the parameters are set
# plt.subplots_adjust(
#   top=0.951,
#   bottom=0.062,
#   left=0.012,
#   right=0.988,
#   hspace=0.249,
#   wspace=0.0
# )
plt.show()