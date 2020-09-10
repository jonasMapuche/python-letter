print('demonstração')
import sys
print('python: {}'.format(sys.version))
import scipy
print('scipy: {}'.format(scipy.__version__))
import numpy
print('numpy: {}'.format(numpy.__version__))
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
import pandas
print('pandas: {}'.format(pandas.__version__))
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
print('* shape: ' + str(dataset.shape))
print('* head (20)')
print(dataset.head(100))
print('* describe')
print(dataset.describe())
print('* groupby')
print(dataset.groupby('class').size())
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
import matplotlib.pyplot as plt
plt.show()
dataset.hist()
plt.show()
from pandas.plotting import scatter_matrix
scatter_matrix(dataset)
plt.show()
array = dataset.values
x = array[:,0:4]
print('* x')
print(x)
y = array[:,4]
print('* y')
print(y)
validationSize = 0.20
seed = 7
from sklearn import model_selection
xTrain, xValidation, yTrain, yValidation = model_selection(x, y, test_size=validationSize, ramdon_state=seed)
scoring = 'accuracy'
