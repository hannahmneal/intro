# This is the Python Stock Dictionary exercise from the NSS curriculum.
#------------------------------------------------------------------------------------------------------------

# Instructions:
# A block of publicly traded stock has a variety of attributes. Let's look at a few of them. A stock has a ticker symbol and a company name. Create a simple dictionary with ticker symbols and company names.

# Example
# stockDict = { 'GM': 'General Motors',
#  'CAT':'Caterpillar', 'EK':"Eastman Kodak" }
# Create a simple list of blocks of stock. These could be tuples with ticker symbols, number of shares, dates and price.

# Example
# purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
#  ( 'CAT', 100, '1-apr-1999', 24 ),
#  ( 'GE', 200, '1-jul-1998', 56 ) ]
# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.

# Example output for one block: I purchased General Electric stock for $4800

# Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

# Example output:

# ------ GE ------
#     ('GE', 100, '10-sep-2001', 48)
#     ('GE', 200, '1-jul-1998', 56)
# Total value of stock in portfolio: $16000

#------------------------------------------------------------------------------------------------------------

stockDict = dict()
stockDict = { 'GM': 'General Motors', 'CAT':'Caterpillar', 'EK':"Eastman Kodak" }
stockDict['GE'] = 'General Electric'
print(stockDict)

purchases = tuple()
purchases = [ ( 'GE', 100, '10-sep-2001', 48 ), ( 'CAT', 100, '1-apr-1999', 24 ), ( 'GE', 200, '1-jul-1998', 56 ), ('GM', 25, '26-may-2019', 14), ('EK', 10, '20-july-2018', 3) ]
print(purchases)

# Full purchase price = shares x dollars for one of the stockDict items

def loop_purchases:
    for purchase in purchases:
        if purchase[0] == 'GE':
            print(purchase)
            return purchase




