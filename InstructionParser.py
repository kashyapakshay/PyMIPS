import re

from InstructionLookup import InstructionLookup
from Utils import Utils

class BaseInstruction(object):
    def __init__(self, instrRegex):
        self.instrRegex = re.compile(instrRegex)

    def parseInstr(self, instr):
        match = self.instrRegex.match(instr)
        if not match:
            return '', ()

        groups = filter(lambda x: x is not None, match.groups())
        operator = groups[0]
        operands = groups[1:]

        return operator, operands

class RTypeInstruction(BaseInstruction):
    def __init__(self):
        RTypeRegex = r'(\w+)\s+(\$\d+)\s+(\$\d+)\s+(\$\d+)'
        super(RTypeInstruction, self).__init__(RTypeRegex)

    def parseInstr(self, instr):
        return super(RTypeInstruction, self).parseInstr(instr)

class ITypeInstruction(BaseInstruction):
    def __init__(self):
        ITypeRegex = r'(\w+)\s+(\$\d+)\s?,?\s+(\$\d+)\s?,?\s+(\d+)|(\w+)\s+(\$\d+)\s?,?\s+(-?\d+)\((\$\d+)\)'
        super(ITypeInstruction, self).__init__(ITypeRegex)

    def parseInstr(self, instr):
        operator, operands = super(ITypeInstruction, self).parseInstr(instr)
        if operator == 'sw' or operator == 'lw':
            return operator, (operands[0], operands[2], operands[1])

        return operator, operands

class JTypeInstruction(BaseInstruction):
    def __init__(self):
        JTypeRegex = r'(\w+)\s+(\w+)'
        super(JTypeInstruction, self).__init__(JTypeRegex)

    def parseInstr(self, instr):
        return super(JTypeInstruction, self).parseInstr(instr)

class InstructionParser:
    def __init__(self, labelsMap={}):
        self.instrObjMap = {
            'R-TYPE': RTypeInstruction,
            'I-TYPE': ITypeInstruction,
            'J-TYPE': JTypeInstruction
        }

        self.formatFuncMap = {
            'binary': lambda s, n: Utils.int2bs(s, n),
            'hex': lambda s, n: Utils.bs2hex(Utils.int2bs(s, n))
        }

        self.labelsMap = labelsMap

        self.instrLookup = InstructionLookup()
        self.instrObj = None

    def extractLabels(self, instr):
        if not instr:
            return '', ''

        split = instr.split(':', 1)

        if len(split) < 2:
            return '', instr

        return split[0], split[1].strip()

    def parse(self, instr):
        label, instr = self.extractLabels(instr)
        if not instr:
            return '', '', None

        operator = instr.split(' ')[0]
        instrType = self.instrLookup.type(operator)
        if not instrType:
            return '', '', None

        instrObj = self.instrObjMap[instrType]()
        operator, operands = instrObj.parseInstr(instr)

        if label:
            operands = list(operands)
            if label not in self.labelsMap:
                operands[-1] = None

            operands[-1] = str(self.labelsMap[label])
            operands = tuple(operands)

        return instrType, operator, operands

    def convert(self, instr, format='binary', formatFunc=None, instrFieldSizes=(6, 4, 4, 4)):
        if not instr:
            return ''

        if formatFunc is None:
            formatFunc = self.formatFuncMap[format]

        instrType, operator, operands = self.parse(instr)
        if not operator:
            return ''

        opcode = self.instrLookup.opcode(operator)
        convertedOpcode = formatFunc(opcode, instrFieldSizes[0])
        operands = map(lambda op: op.strip('$'), operands)
        convertedOperands = map(lambda (i, s): formatFunc(s, instrFieldSizes[i + 1]), enumerate(operands))

        convertedOutput = convertedOpcode + ''.join(convertedOperands)
        return convertedOutput

if __name__ == '__main__':
    # Test
    ip = InstructionParser()
    print ip.convert('add $6 $2 $4')
    print ip.convert('addi $2 $0 2', format='binary')
    print hex(int(ip.convert('addi $2 $0 2', format='binary'), 2))
