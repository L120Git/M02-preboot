from funciones1nivel import sumaTodos

doble = lambda x: x*2
triple = lambda x: x*3

print(sumaTodos(3, doble and triple))
# print(sumaTodos(3, lambda x: x*2)), es lo razonable, es autoexplicativo
print(sumaTodos(100, triple))
# print(sumaTodos(100, lambda x: x*3)), es lo razonable para un uso único

#mod