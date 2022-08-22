from operator import is_
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib as mpl
from database import database_data

def caluclate_increase(data) -> dict():
    data_dict = {
        "date": list(),
        "viewCount": list(), 
        "likeCount": list(), 
        "commentCount": list()
    }
  
    for i in range(0, len(data["date"]) - 1):
        data_dict["date"].append(i + 1)
        data_dict["viewCount"].append(data["viewCount"][i + 1] - data["viewCount"][i])
        data_dict["commentCount"].append(data["commentCount"][i + 1] - data["commentCount"][i])
        data_dict["likeCount"].append(data["likeCount"][i + 1] - data["likeCount"][i])

    return data_dict

def show_graphs(video) -> None:
    data = database_data(video)

    increase_data = caluclate_increase(data)

    x = data["date"]
    y1 = data["viewCount"]
    y2 = data["commentCount"]
    y3 = data["likeCount"]

    mpl.rcParams['toolbar'] = 'None'

    fig, axs = plt.subplots(2, 3, figsize=(17, 7), layout="constrained")
    fig.canvas.manager.set_window_title('Girls Camerwork Guide Video Stats')
    fig.suptitle("Girls Camerwork Guide Video Stats", fontsize="xx-large")

    plot,  = axs[0, 0].plot(x, y1, color="red", marker='o')
    axs[0, 0].set_xlabel("Date")
    axs[0, 0].set_ylabel("Views Count")  

    axs[0, 1].plot(x, y2, color="green", marker='o')
    axs[0, 1].set_xlabel("Date")
    axs[0, 1].set_ylabel("Comments Count")
    #axs[1].yaxis.set_major_locator(ticker.MultipleLocator(1))

    axs[0, 2].plot(x, y3, color="blue", marker='o')
    axs[0, 2].set_xlabel("Date")
    axs[0, 2].set_ylabel("Likes Count")

    x = increase_data["date"]
    y1 = increase_data["viewCount"]
    y2 = increase_data["commentCount"]
    y3 = increase_data["likeCount"]

    axs[1, 0].scatter(x, y1, color="red")
    axs[1, 0].set_ylabel("Views Increase over days")   
    axs[1, 0].xaxis.set_major_locator(ticker.MultipleLocator(1))

    axs[1, 1].scatter(x, y2, color="green")
    axs[1, 1].set_ylabel("Comments Increase over days")
    axs[1, 1].xaxis.set_major_locator(ticker.MultipleLocator(1))

    axs[1, 2].scatter(x, y3, color="blue")
    axs[1, 2].set_ylabel("Likes Increase over days")
    axs[1, 2].xaxis.set_major_locator(ticker.MultipleLocator(1))
    
    for ax in axs[0]:
        ax.ticklabel_format(axis='y', useOffset=False, style='plain')
    for ax in axs[1]:
        ax.ticklabel_format(axis='y', useOffset=False, style='plain')

    plt.show()
    #return fig

# TODO: add this for each graph
    # annotation = axs[0, 0].annotate(text='', xy=(0, 0), xytext=(10, 10),textcoords='offset points', 
    #                                 bbox={'boxstyle': 'round', 'fc': 'w'},
    #                                 arrowprops={'arrowstyle': '->'}) 
    # annotation.set_visible(False)

    # def update_annotation(ind):
    #     x,y = plot.get_data()
    #     annotation.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
    #     text = "{}, {}".format(x[ind["ind"][0]], y[ind["ind"][0]])
    #     annotation.set_text(text)

    # def hover(event):
    #     annotation_visibility = annotation.get_visible()
    #     if event.inaxes == axs[0, 0]:
    #         is_contained, annotation_index = plot.contains(event)
    #         if is_contained:
    #             update_annotation(annotation_index)
    #             annotation.set_visible(True)
    #             fig.canvas.draw_idle()
    #         else:
    #             if annotation_visibility:
    #                 annotation.set_visible(False)
    #                 fig.canvas.draw_idle()

    # fig.canvas.mpl_connect('motion_notify_event', hover)