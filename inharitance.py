# class baba:
#     car="BMW"
#     tk="10000000"
#     house="duplex"

# class kaka(baba):
#     brokencar="tata" 
#     brokenhouse=""

# print(kaka.car)
import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)