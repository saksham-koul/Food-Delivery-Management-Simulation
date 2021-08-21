# Food Delivery Management Simulation

## Abstract 

The days of calling into a restaurant to speak with a rude host are finally over. Whether its constantly being put on hold or having to scream your order through the deafening background noise, ordering food has always been a hassle.
Well thankfully, there’s hope, thanks to some amazing on-demand food delivery service apps! With just a few taps on the screen, we now have access to hundreds of new restaurants and delicious cuisines of every kind one can think of.
Food delivery apps like Swiggy and Zomato allow one to order from a wide range of restaurants and across a wider distance range than most restaurants may organically offer. Contact – less delivery options have also helped cut down the need to stand at the door and wait.

The simulation project _**“Food Delivery Management System”**_ is an attempt to model the food delivery system that is prevalent nowadays through online applications like Swiggy, Zomato, Uber Eats, etc.
The project is visualised from a manager’s/ application’s perspective, who/ which has to deal with customer orders for different associated restaurants.
The objective of the project is to estimate the order delivery time given the number of employees (chefs/ delivery executives) in/ near the restaurant, which can then be relayed to the customer.

## Simulation Algorithm

The project code has been written for modelling a Pizza Delivery Chain in a city (SK Pizza Delivery Chain).
The following algorithm was brainstormed to write the code for the project, so as to ensure the process is an accurate reflection of what customers will really experience:

1. On invoking the program, the user (manager) is given 2 choices to choose from –
    1. To place a new order / enter details of a new order.
    2. Exit the program.

2. On choosing the first option, the program displays the list of branches of the pizza food chain in the city, divided into various zones. (North, South, East, West and Central).

3. Based on the user (manager) input, the branch of the pizza chain from where the order will be relayed is decided.

4. Time required to prepare the order is based on the number of chefs available in the restaurant at that moment, which is a random number in a small range.

5. Delivery time is based on the number of delivery executives available at the time, which is again random, but in a small range.

6. Since both chefs and the delivery executives are shared resources i.e. multiple customers (orders) will be using the same chefs and delivery executives, some waiting behaviour has also been introduced in the program.

7. For every order, the simulation runs on multiple sample cases and finally returns the average time that will be required to deliver the order to the customer, which is a fair estimate when compared to real world scenarios.

## Implementation

* The code for implementing the project has been written in Python.
* Standard Python libraries like _simpy_, _random_, _statistics_ and _time_ have been used.
    * _**Simpy**_ module has been used to create the simulation environment and create the required resources (chefs and delivery executives).
    * _**Random**_ module has been employed to achieve some randomness in the program, in terms of determining the time required to prepare and deliver the order, number of chefs and delivery executives available, etc.
    * _**Statistics**_ module has been used to calculate the mean time required for order delivery over a number of sample cases generated internally by the program for a particular query/order.
    * _**Time**_ module has been employed to determine the durations for various events in the simulation like order preparation time, time required to comply with hygiene protocols (again modelling with the current real – world scenario), time required to deliver the order etc.

* Object – Oriented Programming paradigm has been employed, through the formation of class ‘restaurant’ and its object ‘restro’.
* Generators and the yield statement have been amply used.
* Main inputs to the program –
    * Delivery zone (North, South, East, West or Central) to decide the branch.
    * Order details (types of pizzas along with their quantities).
    * Delivery address
    
* Program Output –
    * Order details with amount payable.
    * Order delivery time, estimated through simulation.
