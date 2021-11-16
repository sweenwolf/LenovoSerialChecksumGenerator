import string


def calculate_checksum(m_id, s_no):
    s_no_list = []
    m_id_list = []
    serial_no = s_no.removeprefix("WB").strip()
    machine_id = m_id.removeprefix("S").strip()
    c_no_comp_list = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(serial_no), 1):
        s_no_list.append(int(serial_no[i: i + 1]))

    for i in range(0, len(machine_id), 1):
        m_id_list.append(int(machine_id[i: i + 1]))

    [reduce_to_zero(x, y) for x, y in zip(s_no_list, c_no_comp_list)]
    [reduce_to_zero(x, y) for x, y in zip(m_id_list, c_no_comp_list)]

    check_sum = 147 - steps
    print("BIOS Checksum is :")
    print("Hex :", hex(check_sum)[2:], ", Ascii :", chr(check_sum))


def reduce_to_zero(new_num, org_num):
    global steps
    res_num = 0
    if new_num != org_num:
        res_num = new_num - org_num

    steps += res_num


def ask4SerialInfo():
    machine_id = input("Please enter Machine ID / Model Name. :")
    serial_no = input("Please enter Serial No. :")
    calculate_checksum(machine_id, serial_no)


if __name__ == '__main__':
    steps = 0
    ask4SerialInfo()
