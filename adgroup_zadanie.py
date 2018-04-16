
def classify_iris(sepal_length, sepal_width, petal_length, petal_width):
    if 0.1 <= petal_width <= 0.6 and 1 <= petal_length <= 1.9 and 2.3 <= sepal_width <= 4.4 and 4.3 <=sepal_length <= 5.8:
        print("setosa")
    if 1 <= petal_width <= 1.8 and 3 <= petal_length <= 5.1 and 2 <= sepal_width <= 3.4 and 4.9 <=sepal_length <= 7:
        print("versicolor")
    if 1.4 <= petal_width <= 2.5 and 4.5 <= petal_length <= 6.9 and 2.2 <= sepal_width <= 3.8 and 4.9 <= sepal_length <= 7.9:
        print("virginica")
    else:
        return ("unclassified")



