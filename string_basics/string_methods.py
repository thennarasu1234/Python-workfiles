# dir(str)
# dir("")
# dir('')
dir("""""")

"""
'capitalize', 'casefold', 'center', 'count', 
'encode', 'endswith', 'expandtabs', 'find', 'format',
'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust',
'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
'upper', 'zfill'
"""

# 1. capitalize
# this method will change the first char of the string to uppercase and keeps the other in lowercase
name_1="tennaraSu"
print(name_1)
name_1.capitalize()
print(name_1)

name_2='TENNARASU'
name_2.capitalize()

# 2. Casefold
# it converts to lowercase
name_3="tennarasu"
name_3.casefold()

# 3. center
# this will makkes the string to be at center 
name_4="tennarasu"
name_4.center(15,"*")

# 4. Count

name_4="tennarasu"

para_2="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ac consequat mauris, suscipit venenatis enim. Proin pretium dolor ac molestie vestibulum. Quisque ante nulla, rhoncus vitae libero vitae, pharetra sagittis leo. Suspendisse sit amet mi vitae lacus faucibus pharetra. Suspendisse lacus leo, molestie vitae orci eget, cursus laoreet odio. Quisque congue dui metus, quis elementum tortor euismod vel. Vivamus varius lorem id sem pellentesque consequat.

Sed ac mattis orci.\nInteger congue nisl nisi, mattis hendrerit sapien eleifend ut. \nNullam imperdiet augue vel tortor aliquam, eget pharetra magna convallis. Sed volutpat lacinia purus vehicula dignissim. Nam ultrices turpis et leo malesuada, ut porta diam euismod. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque feugiat fermentum eleifend. Pellentesque quis maximus lorem.

Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. \nInteger viverra sapien quis purus efficitur, sed viverra nibh tempus. Aenean dapibus viverra lobortis. Aliquam viverra consequat dui cursus pellentesque. Morbi hendrerit ut turpis non imperdiet. Cras cursus imperdiet orci, ut molestie orci hendrerit ut. Nulla viverra fermentum ligula, eu consequat quam porta id. Proin posuere, turpis quis tincidunt eleifend, tellus dui posuere mi, vel scelerisque urna purus quis metus. Nam erat purus, ultricies et gravida sed, consequat ac neque. Mauris arcu velit, consectetur sit amet nulla a, congue fringilla ligula. Nunc rhoncus vitae augue at pharetra. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin id velit nec nibh bibendum commodo. Maecenas sodales id lacus ut dignissim. Proin vel enim id justo dignissim aliquet.

Proin et auctor risus, eget sagittis turpis. \n ullam eget nisl commodo, dapibus ante sit amet, tincidunt nunc. Curabitur scelerisque sapien ac metus porta, id tempus odio luctus. Ut in mollis lectus, sed pretium nibh. Duis maximus, nibh sit amet scelerisque finibus, libero lorem fringilla augue, a blandit nisi orci tincidunt tellus. Cras eleifend purus ipsum, at ullamcorper leo lacinia sit amet. Fusce congue non est vel pharetra. Aliquam erat volutpat. Donec sed feugiat erat, sit amet commodo ipsum. Pellentesque maximus rhoncus efficitur. Vestibulum lobortis in erat sit amet elementum. Etiam metus nisi, ornare at velit non, euismod ultricies justo. Maecenas pharetra risus luctus erat tristique, ac pulvinar nisi lacinia.
"""
para_2.count("s")
# with start
para_2.count("s",20)

# with end
para_2.count("s",20,35)

# 5. endswith

name_6="tennarasu"
name_6.endswith("tenn",0,4)

# complete all the methods with proper explanation commands