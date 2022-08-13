import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Python Tricks", page_icon=":snake:", layout="wide")

def load_lottie_url(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ------ ANIMATIONS ------
lottie_coding = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_huwt6lxv.json")

# ------ HEADER SECTION ------
left_column, right_column = st.columns(2)
#with right_column:
st_lottie(lottie_coding, height=120, key="coding")

with st.container():
    
    st.subheader("Hi, I am Daniela Chambilla :yellow_heart:")
    st.markdown("***First Tutorial in STREAMLIT***")
    st.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier")
    st.subheader("Simple but effective tips for every python lovers")


from PIL import Image
image = Image.open("img/Mr_Pineapple.jpg")
st.image(image, caption="""Photo by [Miesha Maiden](https://www.pexels.com/@miphotography?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels) from [Pexels](https://www.pexels.com/photo/pineapple-with-brown-sunglasses-459601/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)""")
st.caption("Photo by [Miesha Maiden](https://www.pexels.com/@miphotography?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels) from [Pexels](https://www.pexels.com/photo/pineapple-with-brown-sunglasses-459601/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)")
#st.image(image, caption=(st.write("Photo by"), st.write("[Miesha Maiden](https://www.pexels.com/@miphotography?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)")))
#st.write("[Learn More >](https://pranjalai.medium.com/)")
st.write("The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.")

st.write("In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.")


st.write("---")


# ------ WALRUS OPERATOR ------
with st.container():
    st.subheader("1. Walrus operator")
    st.write("The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.")
    
    st.write(":eggplant:*Example*")

    st.write("If we want to check and print the length of a list:")
    
    code = """Mylist = [1,2,3] 
if(l := len(mylist) > 2)
print(l)"""
    st.code(code, language="python")

    st.write(":eggplant:*Output*")

    st.code("3", language="python")

# ------ SPLITTING A STRING ------
with st.container():
    st.subheader("2. Splitting a string")
    st.write("If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!")
    
    st.write(":corn:*Example*")

    code2 = """string = "Hello World"
string.split"""
    st.code(code2, language="python")

    st.write(":corn:*Output*")

    st.code("['Hello', 'World']", language="python")

# ------ REVERSING A STRING ------
with st.container():
    st.subheader("3. Reversing a string")
    st.write("If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.")
    
    st.write(":tomato:*Example*")

    code3 = """str=”hello world!”
a=str[::-1]
print(a)"""

    st.code(code3, language="python")

    st.write(":tomato:*Output*")

    st.code("!dlrow olleh", language="python")

# ------ MERGING TWO DICTIONARIES ------
with st.container():
    st.subheader("4. Merging two dictionaries")
    st.write("This amazing trick will help you merge two dictionaries with just 1 line of code. We just need to use ** in front of the name of the two dictionaries like below two merge them into a single dictionary:")
    
    st.write(":sweet_potato:*Example*")

    code4 = """d1 = {“a”: 10, “b”:20}
d2 = {“c”: 30, “d”:40}
d3 = {**d1, **d2}
print(d3)"""

    st.code(code4, language="python")

    st.write(":sweet_potato:*Output*")

    st.code("{‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}", language="python")

# ------ ZIP() FUNCTION ------
with st.container():
    st.subheader("5. The zip() function")
    st.write("The zip() function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length.")
    
    st.write(":grapes:*Example*")

    code5 = """colour = [“red”, “yellow”, “green”]
fruits = [‘apple’, ‘banana’, ‘mango’]
for colour, fruits in zip(colour, fruits):
print(colour, fruits)"""

    st.code(code5, language="python")

    st.write(":grapes:*Output*")

    st.code("""red apple
yellow banana
green mango""", language="python")

    st.write("The zip() function can also be used for combining two lists into a dictionary. This method can be really helpful while grouping data from the list.")
    
    st.write(":grapes:*Example*")

    code6 = """students = [“Rajesh”, “kumar”, “Kriti”]
marks = [87, 90, 88]
dictionary = dict(zip(students, marks))
print(dictionary)"""

    st.code(code6, language="python")

    st.write(":grapes:*Output*")

    st.code("{‘Rajesh’: 87, ‘kumar’: 90, ‘Kriti’: 88}", language="python")

# ------ ASSIGNING MULTIPLE LIST VALUES TO A VARIABLE ------
with st.container():
    st.subheader("6. Assigning multiple list values to a variable")
    st.write("If you want to assign some specific values of a list to a variable and all the remaining values to another variable in a list format, you can use the following technique:")
    
    st.write(":strawberry:*Example*")

    code7 = """mylist = [1,2,3,4,5]
a,*b = mylist
print(f”a =”,a)
print(f”b =”,b)"""

    st.code(code7, language="python")

    st.write(":strawberry:*Output*")

    st.code("""a = 1
b = [2, 3, 4, 5]""", language="python")

    st.write("This process is also called list unpacking and you can apply this method for more than 2 variables also!")

# ------ REMOVE DUPLICATE LIST ITEMS ------
with st.container():
    st.subheader("7. Remove duplicate list items")
    st.write("Do you have duplicate items in your list which you want to remove? You can do that with only one line of code using the set() function.")
    
    st.write(":pineapple:*Example*")

    code8 = """mylist = [1,1,1,2,2,3,3,4,4,5,6,7,7,8,9]
newlist = set(mylist)
print(newlist)"""

    st.code(code8, language="python")

    st.write(":pineapple:*Output*")

    st.code("{1, 2, 3, 4, 5, 6, 7, 8, 9}", language="python")

# ------ LAMBDA FUNCTION ------
with st.container():
    st.subheader("8. Lambda function")
    st.write("If you need a function that is not very complicated, it can be done easily in one line using lambda. They are also called anonymous functions and are used heavily in data science and web development.")
    
    st.write(":cherries:*Example*")

    st.write("Let’s say you want to write a function to multiply two numbers. Instead of writing a conventional function, you can do that in one line using :")

    code9 = """mul = lambda a,b: a*b
mul(5,6)"""

    st.code(code9, language="python")

    st.write(":cherries:*Output*")

    st.code("30", language="python")

# ------ SWAPPING VARIABLE VALUE ------
with st.container():
    st.subheader("9. Swapping variable value")
    st.write("One of the first programs that we learn while learning about variables is swapping the values of two variables. In python you can achieve that with one line of code:")
    
    st.write(":banana:*Example*")

    code10 = """a = 100
b = 200
a,b = b,a
print(f’a = ‘,a)
print(f’b = ‘,b)"""

    st.code(code10, language="python")

    st.write(":banana:*Output*")

    st.code("""a = 200
b = 100""", language="python")

# ------ USE A PASSWORD IN YOUT CODE ------
with st.container():
    st.subheader("10. Use a password in your code")
    st.write("This python trick is amazing for securing your code with a password. We will use the getpass() function from the library getpass which encodes your input. This will prevent anyone from running the code without a password. Isn’t that cool!")
    
    st.write(":watermelon:*Example*")

    code11 = """from getpass import getpass
password = getpass(“password: “)
if password == “abcd”:
    print(“welcome strnger!”)
else:
    print(“wrong password”)"""

    st.code(code11, language="python")

    st.write(":watermelon:*Output*")

    st.code("""password: **** [abcd]
Welcome stranger!
Password: **** [abdc]
Wrong password""", language="python")

st.write(":blue_book:*Here is [a book](https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922?dchild=1&keywords=automate+the+boring+stuff+with+python&qid=1602697607&sr=8-2&linkCode=sl1&tag=pranjal20-20&linkId=71b2efa5db080e8f74068aebec7d7fb0&language=en_US&ref_=as_li_ss_tl) on Python programming that I would definitely recommend for all beginners.*")

# ------ CONCLUSION ------
with st.container():
    st.subheader("Conclusion")
    st.write("These were a few amazing Python tips and tricks which will make your work a lot easier while coding. There are many more shortcuts like these that you can explore from the official documentation or any other website.")
    
    st.write("*Note: This article contains an affiliate link. This means that if you click on it and choose to buy the resource I linked above, a small portion of your subscription fee will go to me.*")

    st.write("*However, the recommended resource is experienced by me and helped me in my data science career journey.*")

    st.write(":flags:Before you go... ")

    st.write("If you liked this article and want to stay tuned with more exciting articles on Python & Data Science — do consider becoming a medium member by clicking here https://pranjalai.medium.com/membership.")

    st.write("Please do consider signing up using [my referral link](https://pranjalai.medium.com/membership). In this way, the portion of the membership fee goes to me, which motivates me to write more exciting stuff on Python and Data Science.")

    st.write("Also, feel free to subscribe to my free newsletter: [Pranjal’s Newsletter](https://pranjalai.medium.com/subscribe).")

    st.caption("Thanks to Elliot Gunn")
