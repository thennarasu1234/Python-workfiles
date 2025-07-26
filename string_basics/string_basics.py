# double quotes "" string assignment

name_1="Thennarasu"
print(name_1)
name_1

# single quote '' string assignment

name_2='thennarasu'
name_2

#name_3='thennarasu's bag' #-> this statement returns error 
# as ' breaks the string 

name_3="thennarasu's bag"
name_3

# using escape character \
name_3='Thennarsu\'s bag'
name_3

para="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ac consequat mauris, suscipit venenatis enim. Proin pretium dolor ac molestie vestibulum. Quisque ante nulla, rhoncus vitae libero vitae, pharetra sagittis leo. Suspendisse sit amet mi vitae lacus faucibus pharetra. Suspendisse lacus leo, molestie vitae orci eget, cursus laoreet odio. Quisque congue dui metus, quis elementum tortor euismod vel. Vivamus varius lorem id sem pellentesque consequat.

Sed ac mattis orci. Integer congue nisl nisi, mattis hendrerit sapien eleifend ut. Nullam imperdiet augue vel tortor aliquam, eget pharetra magna convallis. Sed volutpat lacinia purus vehicula dignissim. Nam ultrices turpis et leo malesuada, ut porta diam euismod. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque feugiat fermentum eleifend. Pellentesque quis maximus lorem.

Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Integer viverra sapien quis purus efficitur, sed viverra nibh tempus. Aenean dapibus viverra lobortis. Aliquam viverra consequat dui cursus pellentesque. Morbi hendrerit ut turpis non imperdiet. Cras cursus imperdiet orci, ut molestie orci hendrerit ut. Nulla viverra fermentum ligula, eu consequat quam porta id. Proin posuere, turpis quis tincidunt eleifend, tellus dui posuere mi, vel scelerisque urna purus quis metus. Nam erat purus, ultricies et gravida sed, consequat ac neque. Mauris arcu velit, consectetur sit amet nulla a, congue fringilla ligula. Nunc rhoncus vitae augue at pharetra. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin id velit nec nibh bibendum commodo. Maecenas sodales id lacus ut dignissim. Proin vel enim id justo dignissim aliquet.

Proin et auctor risus, eget sagittis turpis. Nullam eget nisl commodo, dapibus ante sit amet, tincidunt nunc. Curabitur scelerisque sapien ac metus porta, id tempus odio luctus. Ut in mollis lectus, sed pretium nibh. Duis maximus, nibh sit amet scelerisque finibus, libero lorem fringilla augue, a blandit nisi orci tincidunt tellus. Cras eleifend purus ipsum, at ullamcorper leo lacinia sit amet. Fusce congue non est vel pharetra. Aliquam erat volutpat. Donec sed feugiat erat, sit amet commodo ipsum. Pellentesque maximus rhoncus efficitur. Vestibulum lobortis in erat sit amet elementum. Etiam metus nisi, ornare at velit non, euismod ultricies justo. Maecenas pharetra risus luctus erat tristique, ac pulvinar nisi lacinia.
"""
para

# for new line \n

para_2="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ac consequat mauris, suscipit venenatis enim. Proin pretium dolor ac molestie vestibulum. Quisque ante nulla, rhoncus vitae libero vitae, pharetra sagittis leo. Suspendisse sit amet mi vitae lacus faucibus pharetra. Suspendisse lacus leo, molestie vitae orci eget, cursus laoreet odio. Quisque congue dui metus, quis elementum tortor euismod vel. Vivamus varius lorem id sem pellentesque consequat.

Sed ac mattis orci.\nInteger congue nisl nisi, mattis hendrerit sapien eleifend ut. \nNullam imperdiet augue vel tortor aliquam, eget pharetra magna convallis. Sed volutpat lacinia purus vehicula dignissim. Nam ultrices turpis et leo malesuada, ut porta diam euismod. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque feugiat fermentum eleifend. Pellentesque quis maximus lorem.

Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. \nInteger viverra sapien quis purus efficitur, sed viverra nibh tempus. Aenean dapibus viverra lobortis. Aliquam viverra consequat dui cursus pellentesque. Morbi hendrerit ut turpis non imperdiet. Cras cursus imperdiet orci, ut molestie orci hendrerit ut. Nulla viverra fermentum ligula, eu consequat quam porta id. Proin posuere, turpis quis tincidunt eleifend, tellus dui posuere mi, vel scelerisque urna purus quis metus. Nam erat purus, ultricies et gravida sed, consequat ac neque. Mauris arcu velit, consectetur sit amet nulla a, congue fringilla ligula. Nunc rhoncus vitae augue at pharetra. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Proin id velit nec nibh bibendum commodo. Maecenas sodales id lacus ut dignissim. Proin vel enim id justo dignissim aliquet.

Proin et auctor risus, eget sagittis turpis. \n ullam eget nisl commodo, dapibus ante sit amet, tincidunt nunc. Curabitur scelerisque sapien ac metus porta, id tempus odio luctus. Ut in mollis lectus, sed pretium nibh. Duis maximus, nibh sit amet scelerisque finibus, libero lorem fringilla augue, a blandit nisi orci tincidunt tellus. Cras eleifend purus ipsum, at ullamcorper leo lacinia sit amet. Fusce congue non est vel pharetra. Aliquam erat volutpat. Donec sed feugiat erat, sit amet commodo ipsum. Pellentesque maximus rhoncus efficitur. Vestibulum lobortis in erat sit amet elementum. Etiam metus nisi, ornare at velit non, euismod ultricies justo. Maecenas pharetra risus luctus erat tristique, ac pulvinar nisi lacinia.
"""
print(para_2)

para_3="Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n p"
print(para_3)

# for tab \t
name_5="Nirmal\tKumar"
print(name_5)

dec=""
dec=''
dec=""""""
dec=str(10) #type conversion from int to string
dec

# strings are indexed

name_3="tennarasu"
# 0,1,2,3,4,5,6,7,8
# -9,-8,-7,-6,-5,-4,-3,-2,-1

# this return the char at that index
name_3[7]

# this return the string from index 1 to the last index
name_3[1:]

# this return the string from index 1 to the last index
# the stop take n-1 as it end
name_3[1:7:2]

# string has negative index
name_3[-8]


# [start,stop,step]

