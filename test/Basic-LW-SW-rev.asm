#Author: John Rieffel
#NOTE: if your instruction word does not support immediates as large as 7,
# you will need to REWRITE this code in order to work with your processor
#
# results: values 0..7 should be in memory locations 0..7
# 	   values 7..0 should be in registers 0..7 (switched)
addi $1 $0 1
addi $2 $0 2
add  $3 $2 $1
add  $4 $2 $2
addi $5 $0 5
add  $6 $2 $4
addi $7 $0 7
sw   $1 1($0)
sw   $2 2($0)
sw   $3 3($0)
sw   $4 3($1)
sw   $5 2($3)
sw   $6 0($6)
sw   $7 7($0)
lw   $0 0($7)
lw   $1 -1($7)
lw   $2 -2($7)
lw   $3 -3($7)
lw   $4 -4($7)
lw   $5 -5($7)
lw   $6 -6($7)
lw   $7 -7($0)
