#10	Self-Checkout

Working with multiple inputs and currency can introduce some tricky precision issues.

Create a simple self-print_invoice system. Prompt for the prices and quantities of three items. Calculate the subtotal of the items. Then calculate the tax using a tax rate of 5.5%. Print out the line items with the quantity and total, and then print out the subtotal, tax amount, and total.

Example Output

```​ 	
Enter the price of item 1: 25
Enter the quantity of item 1: 2
Enter the price of item 2: 10
Enter the quantity of item 2: 1
Enter the price of item 3: 4
Enter the quantity of item 3: 1
Subtotal: $64.00
Tax: $3.52
Total: $67.52
```

## Constraints

Keep the input, processing, and output parts of your program separate. Collect the input, then do the math operations and string building, and then print out the output.

Be sure you explicitly convert input to numerical data before doing any calculations.

## Challenges

Revise the program to ensure that prices and quantities are entered as numeric values. Don’t allow the user to proceed if the value entered is not numeric.

Alter the program so that an indeterminate number of items can be entered. The tax and total are computed when there are no more items to be entered.


## Solution 

### Python

Wrote `self_checkout.py` and `cart.py`, with associated tests.

```

Invoice:
-----------------------------------------------------------------------------------------------------------
 Item  Description                    Quantity   Unit Price   Line Price  
 

     1 item 1                                  1        $2.99        $2.99

 

     2 item 2                                  3        $0.55        $1.65

 

     3 item 3                                 10        $0.10        $1.00

 
-----------------------------------------------------------------------------------------------------------
 Subtotal:        $5.64
 Taxes:           $0.31
 Total:           $5.95

```

### Learnings

* create a python package, with an `__init__.py` empty file, then import from `package_folder.file`

* formatting language

* found recipe for formatting money

* use `decimal.Decimal` for money stuff, but have to use it *everywhere*

* mocking `sys.stdin` using `StringIO`

* using `MagicMock` to test calls

### Desires

I want something like Ruby Enumerable's `each_with_index` so I don't have to resort to using a `for i in range(...)`
to run through a list while keeping track of the index.

Better way of formatting table-type output. This all goes away in HTML, of course.

