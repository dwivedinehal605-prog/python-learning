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
  #Topic3: Tuples
  #Q7: Create a tuple point = (12, 5). Print each value with a label (x and y).
point=(12,5)
print("tuple:",point)
print("x=",point[0])
print("y=",point[1])
print()
 #Q8: Try to change the first value of the tuple to 99. Write down what happens and explain why in one line.
point=(12,5)
print("tuple:",point)
print("it is not able to change the first value of tuple because tuple is immutable.")
print()
 #Topic4: Sets
 # Q9. Given colours = ["red","green","blue","green","red"], use a set to find how many distinct colours there are.
colours = ["red","green","blue","green","red"]
print("set:",colours)
distinct_colours=set(colours)
print("distinct colours:",distinct_colours)
print("number of distinct colours:",len(distinct_colours))
print() 
 #Q10. Two students' subjects: asha = {"ML","Maths","Python"} and ravi = {"Python","Stats"}. Find (a) all subjects either studies, and (b) subjects they both study.
asha = {"ML","Maths","Python"}
ravi = {"Python","Stats"}
print("first set:",asha)
print("second:",ravi)
print("common subjects in both sets:",asha&ravi)
print("all subjects they study:",asha|ravi)
print() 
#Topic5: Dictionary
#Q11.Build a dictionary describing a book with keys title, author, year. Print the author by key.
book={"title":"self love","author":"nehal dwivedi","year":"2020"} 
print("dictionary:",book)
print("author name:",book["author"])
print()
 #Q12: Add a new key pages to the book, update the year, then print all key–value pairs using items().
book={"title":"self love","author":"nehal dwivedi","year":"2020"} 
print("dictionary:",book)
book["pages"]=200
book["year"]=2022
print(book.items())
print()
 #Q13. Use get() to look up a key that does NOT exist (e.g. "publisher") and show that it returns None instead of an error.
book={"title":"self love","author":"nehal dwivedi","year":"2020"} 
print("dictionary:",book)
print(book.get("publisher"))
print()
 # Challenge (combine everything)
 #Q14. You are given a list of repeated city names: cities = ["Pune","Delhi","Pune","Surat","Delhi","Pune"]. (a) Use a set to get the unique cities. (b) Build a dictionary that maps each unique city to how many times it appears in the list. (Hint: loop and use count() or get().)
# (a) Unique cities using a set
cities = ["Pune","Delhi","Pune","Surat","Delhi","Pune"]
print("list:",cities)
distinct_cities=set(cities)
print("unique cities in set:",distinct_cities)
print()
# (b) Dictionary to count occurrences
city_count={}
for city in cities:
    city_count[city]=city_count.get(city,0)+1
print("city counts:",city_count)



    
