from sklearn.datasets import fetch_20newsgroups
twenty_train = fetch_20newsgroups(subset='train', categories=None, shuffle=True, random_state=42)

print(twenty_train.target_names)

print(f'numer of training data is {len(twenty_train.data)}')

print(f'numer of training data files is {len(twenty_train.filenames)}')

print("\n".join(twenty_train.data[0].split("\n")[:3]))

print(twenty_train.target_names[twenty_train.target[0]])

print(f'target = {twenty_train.target[:10]}')

for t in twenty_train.target[:10]:
	print(twenty_train.target_names[t])
