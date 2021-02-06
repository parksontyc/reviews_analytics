
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data)) #每讀1000筆印一次
print(len(data))
print(data[0])
print('-----------------------------')
print(data[1])

sum_len = 0
for i in data:
	sum_len = sum_len + len(i)
	#print(sum_len)
avg = sum_len / len(data)
print(avg)

new = []
for i in data:
	if len(i) <= 100:
		new.append(i)
		#print(len(new))
print('共有', len(new), '筆資料小於100')

word = []
for i in data:
	if 'good' in i:
		word.append(i)
print('總共有', len(word), '筆資料裡面含有good字串')

word = [i for i in data if "good" in i]
print('總共有', len(word), '筆資料裡面含有good字串')
