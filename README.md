
### Developed by Sai Teja Macharla 
#### *Email: macharlasaiteja@gmail.com*  

<br>

#### No Test cases provided for this Assignment.
<br>

#  Session 13 - Generators and Iteration Tools
## Topics Covered 
- Yielding and Generator Functions
- Making an iterable from a Generator
- Generator Expressions and Performance
- Yield From
- Aggregators
- Slicing
- Selecting and Filtering
- Infinite Iterators
- Chaining and Teeing
- Mapping and Reduction
- Zipping


## **Project: Description** 
We have two goals:

#### **Goal 1**
- Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate - i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer, then it should be stored as an integer, etc.

#### **Goal 2**
- Calculate the number of violations by car make.

#### **Note** :
Try to use lazy evaluation as much as possible - it may not always be possible though! That's OK, as long as it's kept to a minimum.
- No Test Cases




![](/ "")

## **Function created based on Assignment**

### **records_generator** :
- Generator for traffic violations named tuple


### **fetch_records** :
- returns list of NamedTuple for traffic violations


### **vehicle_make_information** :
- Generator for Vehicle Make from given records

### **vehicle_make_violations** :
- Generator for traffic violations by Vehicle Make

### **show_violations** :
- Prints Vehicle Make and Traffic Violations in tabular format