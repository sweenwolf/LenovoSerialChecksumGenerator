def __str2int(value):
    try:
        val = int(value)
        if isinstance(val, int):
            return val
        else:
            return 0
    except ValueError:
        return 0


def __calc_checksum(value):
    steps = 0

    for num in value:
        steps += __str2int(num)

    return steps


if __name__ == '__main__':
    
    machine_id = input("Please enter Machine ID / Model Name. :")
    serial_no = input("Please enter Serial No. :")

    checksum = 147 - __calc_checksum(machine_id) - __calc_checksum(serial_no)
    print("BIOS Checksum = Hex :", hex(checksum)[2:], ", Ascii :", chr(checksum))
