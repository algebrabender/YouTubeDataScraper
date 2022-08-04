import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from database import database_data

def caluclate_increase(data) -> dict():
    data_dict = {
        "date": list(),
        "viewCount": list(), 
        "likeCount": list(), 
        "commentCount": list()
    }
  
    for i in range(0, len(data["date"]) - 1):
        data_dict["date"] = i + 1
        data_dict["viewCount"].append(data["viewCount"][i + 1] - data["viewCount"][i])
        data_dict["commentCount"].append(data["commentCount"][i + 1] - data["commentCount"][i])
        data_dict["likeCount"].append(data["likeCount"][i + 1] - data["likeCount"][i])

    return data_dict

def show_graphs() -> None:
    data = database_data()

    increase_data = caluclate_increase(data)

    x = data["date"]
    y1 = data["viewCount"]
    y2 = data["commentCount"]
    y3 = data["likeCount"]

    fig, axs = plt.subplots(1, 3, figsize=(15, 5), layout="constrained")
    fig.suptitle("Girls Camerwork Guide Video Stats", fontsize="xx-large")

    axs[0].scatter(x, y1, color="red")
    axs[0].set_xlabel("Date")
    axs[0].set_ylabel("Views Count")   

    axs[1].scatter(x, y2, color="green")
    axs[1].set_xlabel("Date")
    axs[1].set_ylabel("Comments Count")
    axs[1].yaxis.set_major_locator(ticker.MultipleLocator(1))

    axs[2].scatter(x, y3, color="blue")
    axs[2].set_xlabel("Date")
    axs[2].set_ylabel("Likes Count")

    for ax in axs:
        ax.ticklabel_format(axis='y', useOffset=False, style='plain')
    plt.show()

    #TODO: change to seperate plot so both show at the same time

    x = increase_data["date"]
    y1 = increase_data["viewCount"]
    y2 = increase_data["commentCount"]
    y3 = increase_data["likeCount"]

    fig, axs = plt.subplots(1, 3, figsize=(15, 5), layout="constrained")
    fig.suptitle("Girls Camerwork Guide Video Stats", fontsize="xx-large")

    axs[0].scatter(x, y1, color="red")
    axs[0].set_ylabel("Views Count")   
    axs[0].xaxis.set_major_locator(ticker.MultipleLocator(1))

    axs[1].scatter(x, y2, color="green")
    axs[1].set_ylabel("Comments Count")
    axs[1].xaxis.set_major_locator(ticker.MultipleLocator(1))
    axs[1].yaxis.set_major_locator(ticker.MultipleLocator(1))

    axs[2].scatter(x, y3, color="blue")
    axs[2].set_ylabel("Likes Count")
    axs[2].xaxis.set_major_locator(ticker.MultipleLocator(1))

    for ax in axs:
        ax.ticklabel_format(axis='y', useOffset=False, style='plain')
    plt.show()

    print(increase_data)
    

show_graphs()