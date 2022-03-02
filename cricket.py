weather=['sunny','sunny','overcast','rainy','rainy','rainy','overcast','sunny','sunny','rainy','sunny','overcast','overcast','rainy']
temp=['hot','hot','hot','mild','cool','cool','cool','mild','cool','mild','cool','mild','mild','mild','hot','mild']
play=['no','no','yes','yes','yes','no','yes','no','yes','yes','yes','yes','yes','no']
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
weather_encoded=le.fit_transform(weather)
print(weather_encoded)
temp_encoded=le.fit_transform(temp)
label=le.fit_transform (play)
print("Temp:",temp_encoded)
print("Play:",label)
features=list(zip(weather_encoded,temp_encoded))
print(features)
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(features,label)
print(" sunny-2 overcast-1 rainy-0")
print("hot-1 mild-2 cool-0")
a=int(input("enter weather"))
b=int(input("enter temp"))
predicted=model.predict([[a,b]])
print("predicted value:",predicted)
if predicted==1:
 print("There will be a play today")
else:
 print("There will be no play today")


