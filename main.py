import statistics
import random
import pandas as pd

df = pd.read_csv("data.csv")
data = df["Math_score"].tolist()


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


meanList = []
for i in range(0,100):
    setOfMeans= random_set_of_mean(30)
    meanList.append(setOfMeans)

print("mean of sampling distribution:- ",statistics.mean(data))
print("Population Mean ", statistics.mean(meanList))
