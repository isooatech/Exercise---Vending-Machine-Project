# Vending-Machine-Project

The code simunlates how a vending machine works.

The functionality details are provided below

Admin login: 
This option will simulate how the vending machine operator validates their credentials. When this option is selected, the user should be prompted to input their username and password. The username should be admin and the password is be any number smaller than 10. You should allow the user to try four times, if all of them are incorrect, then the program stops and the program cell needs to be run again.
Note: 
Once that an admin has logged in, this option has to be disabled (i.e. the user cannot go back and select this option).

Add products: 
This option can only be accessed once option 1 has been completed, otherwise the message login first! should be displayed and the program should go back to the main menu. In this option, the admin will be shown the list of snacks and categories in the vending machine. Then, the admin can input a machine code slot to add one more product for that certain slot. Afterwards, the program should show the new stock and go back to the main menu.
Note: Keep in mind that each space in the vending machine can hold a maximum of eight products (of the same snack, of course). Also, you cannot add products in the empty slots. Therefore, your program should warn the admin in case that they want to add more products of a specific snack in a slot, or if the admin wants to add products in an empty slot.

Buy snacks: 
This option can be accessed by "anyone", so there is no need for a validation. If this option is selected, the user will be shown the list of snacks, amounts and prices. Then, the user will be requested to select one snack based on the machine_code. Once the snack is selected, your program must display the price of the selected product. Then, the user will be prompted to pay. To simulate this payment, you will ask the user for an input and write any positive number (if the user inputs something invalid, ask to try again). Then, your program must check this number against the price of the product to be bought. If the input number is larger than the price, then you should return your change is... and the subtraction of the payment minus the price of the snack. If the number is equal to the price, then you must return thanks for paying. Else, you should output you need to pay more and allow the user to write another amount. After the "purchase", you should output to the user the number of products left for that particular snack (therefore, you need to update the data frame!). Notice that if there were zero products left for the snack selected, then you must prompt this to the user in advance before letting them buy, and ask them to select another snack.

Exit
