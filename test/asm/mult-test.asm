# Author: Akshay Kashyap
# Test mult instruction.
addi $1 $0 1
addi $2 $0 2
mult $3 $1 $2
sw $3 0($0)
