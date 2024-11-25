immutable_var = ([1, 'zv', True])
immutable_var[1] = ('123') # immutable_var являеться картежом и являеться не изменяемым, но можно добавить в картеж список с помощью []
print(immutable_var)
mutable_list = [1, 2, 4, 'age' ]
mutable_list[3]= 'old'
print(mutable_list)