import matplotlib.pyplot as plt
import seaborn as sns

def get_bar_info(data, title, column_x, column_y,label_x="",label_y="", legend=False):
    sns.barplot(
        data=data,
        x=column_x,
        y=column_y,
        hue=column_x,
        legend=legend
    )

    plt.title(title)

    if label_x is None:
        plt.xlabel(column_x)
    else: 
        plt.xlabel(label_x)

    if label_y is None:
        plt.ylabel(column_y)
    else:
        plt.ylabel(label_y)
    plt.show()

def get_bar_number_info(data, title, column_x, column_y,label_x="",label_y="", legend=False):
    ax = sns.barplot(
            data=data,
            x=column_x,
            y=column_y,
            hue=column_x,
            legend=legend
        )

    for container in ax.containers:
        ax.bar_label(container, fmt="%.0f", padding=3)

    plt.title(title)

    if label_x is None:
        plt.xlabel(column_x)
    else: 
        plt.xlabel(label_x)

    if label_y is None:
        plt.ylabel(column_y)
    else:
        plt.ylabel(label_y)
    plt.show()