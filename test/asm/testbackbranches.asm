#assuming all registers are 0
#the loop should run five times
#and registers 1-5 should all contain 5
#anything else, and your branching fails
addi $1 $0 1
addi $1 $0 1
addi $2 $0 1
addi $3 $0 1
addi $4 $0 1
addi $5 $0 5
beq  $1 $5 5   #should only be taken on fifth loop
addi $1 $1 1
addi $2 $2 1
addi $3 $3 1
addi $4 $4 1
beq  $1 $1 -6  #should always be taken, branch back to first beq
