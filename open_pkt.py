import pickle
file = open('ref_name.pkl', 'rb')
data = pickle.load(file)
file.close()
print('Showing the pickled data:')
cnt = 0
for item in data:
    print('The data ', cnt, ' is : ', item)
    cnt += 1