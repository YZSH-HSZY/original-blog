import pyshark

cap_file_path = r'D:\yzsh\all_project\KC2W_DATA_CONVERT_TEST\doc\wireshark_n2k.pcapng'
a_cap = pyshark.FileCapture(cap_file_path)
for a in a_cap:
    print(a.ip_src)