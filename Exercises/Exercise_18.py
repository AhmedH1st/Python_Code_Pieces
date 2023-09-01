# Script to generate Init Function of GPIO for avr in .c file
import os.path


def create_Init_Function():
    ls = []
    pin_val = ""
    for i in range(8):
        pin_val = ""
        while True:
            pin_val = input(f'Please Enter Pin {str(i)} mode (in of out): ')
            if (pin_val not in ['in', 'out']):
                print("wrong entry")
            else:
                ls.append(pin_val)
                break
    return ls


if __name__ == "__main__":

    C_File_Path = os.path.dirname(__file__)
    ls = create_Init_Function()
    for i in range(len(ls)):
        if ls[i] == 'in':
            ls[i] = '0'
        elif ls[i] == 'out':
            ls[i] = '1'
        else:
            pass

    DDRA_Reg = "".join(ls)

    with open(C_File_Path+'/GPIO_init.c', mode='w') as fd:
        fd.write(
            '#include <stdio.h>\n\nvoid GPIO_PoratA_Init(void){\n\n\tDDRA = 0b'+'{}'.format(DDRA_Reg)+';\n}')
