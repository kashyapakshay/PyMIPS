#this assumes that the mechanics for jump 
# offsets use ABSOLUTE address to jump to
# (i.e. that they are not offsets)

# $1 should have the value 3 if this passes tests
# and other values otherwise
addi $1 $0 1
j 7
addi $1 $1 1 
addi $1 $1 1 #line 3,  jump here second, $1 = $1+1 = 3
j 9          #jump out
addi $1 $1 1
addi $1 $1 1
addi $1 $1 1  #line 7, jump here first, $1 = $1+1 = 2
j 3	      #jump to line 3
	      #line 9, done.

