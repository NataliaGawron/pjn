import pandas as pd
from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder

# classifier = DecisionTreeClassifier()
# classifier = RandomForestClassifier()
classifier = AdaBoostClassifier()

dataset = pd.read_csv("mycsvfile2.csv", sep="\t")
dataset.shape
X = dataset.drop('vote_average', axis=1).drop(
    'backdrop_path', axis=1).drop('genres', axis=1).drop('imdb_id', axis=1).drop('homepage', axis=1).drop('belongs_to_collection', axis=1).drop('production_companies', axis=1).drop('production_countries', axis=1).drop('spoken_languages', axis=1)
Y = dataset['vote_average']

lb = LabelEncoder()
le_adult = LabelEncoder()
lb_budget = LabelEncoder()
lb_id = LabelEncoder()
lb_language = LabelEncoder()
lb_tittle = LabelEncoder()
lb_overwie = LabelEncoder()
lb_popularity = LabelEncoder()
lb_poster = LabelEncoder()
lb_release = LabelEncoder()
lb_revenue = LabelEncoder()
lb_runtime = LabelEncoder()
lb_status = LabelEncoder()
lb_tagline = LabelEncoder()
lb_title = LabelEncoder()
lb_video = LabelEncoder()
lb_vote_count = LabelEncoder()

Y = Y.fillna(0.0)
Y = lb.fit_transform(Y)

X['adult'] = le_adult.fit_transform(X['adult'])
X['budget'] = lb_budget.fit_transform(X['budget'])
X['id'] = lb_id.fit_transform(X['id'])
X['original_language'] = lb_language.fit_transform(X['original_language'])
X['original_title'] = lb_tittle.fit_transform(X['original_title'])

X['overview'] = X['overview'].fillna('')
X['overview'] = lb_overwie.fit_transform(X['overview'])

X['popularity'] = lb_popularity.fit_transform(X['popularity'])

X['poster_path'] = X['poster_path'].fillna('')
X['poster_path'] = lb_poster.fit_transform(X['poster_path'])

X['release_date'] = X['release_date'].fillna('')
X['release_date'] = lb_release.fit_transform(X['release_date'])
X['revenue'] = lb_revenue.fit_transform(X['revenue'])

X['runtime'] = X['runtime'].fillna('0')

X['runtime'] = lb_runtime.fit_transform(X['runtime'])
X['status'] = lb_status.fit_transform(X['status'])

X['tagline'] = X['tagline'].fillna('')
X['tagline'] = lb_tagline.fit_transform(X['tagline'])
X['title'] = lb_title.fit_transform(X['title'])
X['video'] = lb_video.fit_transform(X['video'])
X['vote_count'] = lb_vote_count.fit_transform(X['vote_count'])

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.80)


classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

y_report = classification_report(y_test, y_pred)

y_matrix = confusion_matrix(y_test, y_pred)

output = accuracy_score(y_test, y_pred)
print("Accuracy: \n")
print(output)

print("\n Report: \n")
print(y_report)

print("\n Matrix: \n")
print(y_matrix)
