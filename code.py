import plotly.figure_factory as ff
import pandas as pd
import statistics
import random

data = pd.read_csv("data.csv")
data_list = data["reading_time"].tolist()

def random_sample_mean(n):
    dataset = []
    for i in range(0, n):
        rand_index = random.randint(0, (len(data_list)-1))
        value = data_list[rand_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def figure_show(mean_list):
    dataset = mean_list
    figure = ff.create_distplot([dataset], ["reading_time"], show_hist=False)
    figure.show()

def setup():
    mean_list=[]
    for i in range(0, 100):
        means = random_sample_mean(30)
        mean_list.append(means)
    print("sampling mean:- ", statistics.mean(mean_list))    
    figure_show(mean_list)

population_mean = statistics.mean(data_list)
print("population mean:- ", population_mean)
setup()