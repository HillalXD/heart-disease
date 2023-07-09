# heart-disease

This project use to classify if someone have heart problem or not by assign some variable to flask webapp, this project is usefull for give user heart disease

## Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
- [imblearn](https://imbalanced-learn.org/stable/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [fastapi](https://flask.palletsprojects.com/)
- [flask](https://fastapi.tiangolo.com)

## Usage

first, you can clone this git repository

```
git clone https://github.com/HillalXD/heart-disease.git
```

then navigate your command to this directory

```
cd heart-disease
```

after that run `app.py` to use fast api

```
python app.py
```


## Code 
- Template code is provided in the `classification.ipynb` notebook file.
- `heart.csv` is provide data source for training model
- `app.py` is fastapi web application to user input features for model predicting 

## Dataset features

for doing prediction you need to input this features:

| features  | explanation  | 
| :-------- | :------- | 
| BMI | user BMI value |
| smoking  | is user smoker or not |
| stroke  | is user on stroke or not |
| diffwalking   | is user feel difficult to walk or not |
| sex | user gender |
| diabetic | is user diabetic patient or not|
| kidneydisease | is user have disease on kidney or not |
| skincancer | is user have skin cancer or not|




