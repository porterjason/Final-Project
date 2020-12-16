import streamlit as st

hungry = ['not very','somewhat', 'kind of', 'very', 'super']
st.write("How Hungry are You? ")
x = st.slider('Hungry Index',0.0,4.0,1.0)
st.write('You are ', hungry[int(x)], 'hungry!')
st.write(x)

# Add a selectbox :
delivery = st.selectbox(
    'Delivery Option: ',
    ('Eat-In', 'Curb-Side', 'Delivery')
)

st.write("This order is for ", delivery)

if st.button("Click Me"):
    st.write("You clicked me!")
else:
    st.write("Waiting to be clicked")

st.write("Pizza Options")
sizes = ['small','medium','large','extra large']
size = st.radio("Select a size: ", sizes)

mushrooms = st.checkbox("Mushrooms", False)
cheese = st.checkbox("Extra Cheese", True)

if mushrooms and cheese:
    st.write("Your ", size,  " pizza will have mushrooms and extra cheese.")
elif mushrooms:
    st.write("Your ", size,  " pizza will have mushrooms.")
elif cheese:
    st.write("Your ", size,  " pizza will have extra cheese.")
else:
    st.write("Your ", size, " pizza is plain.")

meats = ['Sausage','Meatball','Hamburger','Chicken']
meat_toppings = st.multiselect("Select toppings:", meats)

st.write("We will add: ", meat_toppings)

code = st.number_input("Enter your promotion code: ",0,9999,1)
if  code == "4321":
    st.write("That code is valid!")
else:
    st.write("That code is not valid!")

your_name = st.text_input("Name: ", "Mark")
st.write("Thanks,", your_name, " for your order!")
