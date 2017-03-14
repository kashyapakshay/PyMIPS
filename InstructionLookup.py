class InstructionLookup:
    def __init__(self):
        self.opcodeDict = {
        	'R-TYPE': {
        		'add': 0,
        		'and': 1,
        		'or': 2,
        		'sub': 3,
        		'sgt': 14,
        		'slt': 13,
                'mult': 17
        	},
        	'I-TYPE': {
        		'addi': 4,
        		'andi': 5,
        		'ori': 6,
        		'subi': 7,
        		'lw': 10,
        		'sw': 11,
        		'beq': 9,
        		'bne': 13,
        		'blt': 14,
        		'bgt': 15
        	},
        	'J-TYPE': {
        		'j': 16,
        		'jal': 18,
        		'jr': 19
        	}
        }

    def type(self, operator):
        for k in self.opcodeDict:
            if operator in self.opcodeDict[k]:
                return k

        return ''

    def opcode(self, operator):
        k = self.type(operator)
        if k == '':
            return -1

        return self.opcodeDict[k][operator]
