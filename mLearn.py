import pandas
from pandas.plotting import scatter_matrix
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
print('* shape: ' + str(dataset.shape))
print('* head (20): \n' + str(dataset.head(20)))
print('* describe: \n' + str(dataset.describe()))
print('* groupby: \n' + str(dataset.groupby('class').size()))
array = dataset.values
x = array[:,0:4]
y = array[:,4]
validationSize = 0.20
seed = 7
xTrain, xValidation, yTrain, yValidation = model_selection.train_test_split(x, y, random_state=seed)
print(xTrain.shape)
print(xValidation.shape)
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
dataset.hist()
plt.show()
scatter_matrix(dataset)
plt.show()
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(xTrain, yTrain)
predictions = knn.predict(xValidation)
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
print('* accuracy: ')
print(accuracy_score(yValidation, predictions))
print('* confusion matrix: ')
print(confusion_matrix(yValidation, predictions))
print('* classification report: ')
print(classification_report(yValidation, predictions))