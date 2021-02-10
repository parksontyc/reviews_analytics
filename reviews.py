
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data)) #每讀1000筆印一次
print('檔案讀取完了，總共有', len(data), '筆資料')

print(data[0])

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

while True:
	word = input('請問你要查什麼字：')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word], '次')
	else:
		print('沒有這個字')

print('感謝使用本功能！')









# print(data[0])
# print('-----------------------------')
# print(data[1])

# sum_len = 0
# for i in data:
# 	sum_len = sum_len + len(i)
# 	#print(sum_len)
# avg = sum_len / len(data)
# print(avg)

# new = []
# for i in data:
# 	if len(i) <= 100:
# 		new.append(i)
# 		#print(len(new))
# print('共有', len(new), '筆資料小於100')

# word = []
# for i in data:
# 	if 'good' in i:
# 		word.append(i)
# print('總共有', len(word), '筆資料裡面含有good字串')

# word = [i for i in data if "good" in i]
# print('總共有', len(word), '筆資料裡面含有good字串')

# word = [1 for i in data if 'good' in i] #裝進1
# print('總共有', len(word), '筆資料裡面含有good字串')
# print(word)

# bad = ["bad" in i for i in data] #boolean
# print(bad)