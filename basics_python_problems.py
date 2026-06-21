 #Topic1: Lists
 # Q1: creat a list marks=[72,65,88,900,65]. print its length, the highest mark(hint:max()), and how many times 65 appears.
marks=[72,65,88,90,65]
print("mark:",marks)
print("length of list:",len(marks))
print("max value in the list:",max(marks))
print("number of occurance of 65:",marks.count(65)) 
print()
 # Q2:Append 100 to marks, then sort it in descending order. (Hint: sort(reverse=True).)
marks=[72,65,88,90,65]
x=marks.append(100)
print("append 100 in list:", marks)
y=marks.sort(reverse=True)
print("sort the list in descending order:", marks)
print()
#Q3: Remove the first occurrence of 65 from the list, then print the list.
marks=[72,65,88,90,65]
a=marks.remove(65)
print("remove first occurance of 65:",marks)
print()
 #Topic2: Strings
 #Q4: Given s = "machine learning", print it in title case and in all caps.
s = "machine learning"
print(s)
print("string in title case:",s.title())
print("string in upper case:",s.upper())
print()
 #Q5:Split the sentence "data,model,train,test" on the comma into a list, then join that list back together using a space.
text="data,model,train,test"
print("text:",text)
lst=text.split(",")
result=" ".join(lst)
print("seperate text by comma:",lst)
print("join lst using space:",result)
print()
 #Q6:Count how many times the letter "a" appears in "banana"
b="banana"
x=b.count("a")
print("count a in banana:",x)
print()
 
