import matplotlib.pyplot as plt

# function to plot line graph
def line_graph(x, y, width, height, title, x_label):
    plt.figure(figsize=(width,height))
    plt.plot(x , y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel('Published headline')
    plt.show()