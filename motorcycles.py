#修改列表元素
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

#在列表末尾添加元素
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

lap=[]
lap.append('first')
lap.append('second')
lap.append('third')
print(lap)

#在列表中插入元素
motorcycles=['honda','yamaha','suzuki']

motorcycles.insert(0,'ducati')
print(motorcycles)

#从列表中删除元素 del根据索引删除元素
print('')

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

#pop删除元素，并返回被删除的元素
print('')

nows=['honda','yamaha','suzuli']
print(nows)

poped_nows=nows.pop()
print(nows)
print(poped_nows)

#pop（）根据索引删除元素，并返回被删除的元素
print('')

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

second_owned=motorcycles.pop(1)
print(f'The second notorcycles I owned was a {second_owned.title()}')

#remove根据值删除元素
print('')

motorcycles=['honda','yanmaha','suzuli','ducati']
print(motorcycles)

too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')

