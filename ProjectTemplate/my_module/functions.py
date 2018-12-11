"""A collection of function for doing my project."""

def print_listing(crypt_name_list):
    """
    Function to print the list of crytocurrencies
    
    Parameters
    ----------
    crypt_name_list: list
        List of cryptocurrency the user can select from
    """
    print('CRYPTOCURRENCY LISTING: \n' + 
      '-----------------------\n')
    
    word_counter = 0
    for item in crypt_name_list:
        print(item, end="  ", flush=True)
        word_counter += 1
        
        if word_counter == 4:
            print()
            word_counter = 0
        
def print_keys(crypt_val):
    """
    Function to print the list of attributes for the cryptocurreny selected

    Parameters
    ----------
    crypt_val: list
        List of attributes the user can select from
    """
    print('VALUE LISTING: \n' + '---------------')
    word_counter = 0
    for item in crypt_val:
        print(item, end="  ", flush=True)
        word_counter += 1
        
        if word_counter == 2:
            print()
            word_counter = 0

