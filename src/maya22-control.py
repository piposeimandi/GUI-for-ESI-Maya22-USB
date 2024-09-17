import sys
import hid
import getopt

VENDOR_ID = 0x2573
PRODUCT_ID = 0x0017

# Función para obtener el máximo valor
def max_val(a, b):
    return max(a, b)

# Función para obtener el mínimo valor
def min_val(a, b):
    return min(a, b)

def enumerate_hid():
    devices = hid.enumerate(VENDOR_ID, PRODUCT_ID)
    if devices:
        for device in devices:
            print(f"{device['vendor_id']:04x}:{device['product_id']:04x} - {device['path']} {device['serial_number']}")
            print(f"    vendor: {device['manufacturer_string']}")
            print(f"    product: {device['product_string']}")
    else:
        print("HID dev list is empty")

def send(dev, op, byte):
    buf = [0] * 33  # +1 byte for report id
    buf[1] = 0x12
    buf[2] = 0x34
    buf[3] = op
    buf[5] = 1
    buf[6] = byte
    buf[22] = 0x80
    
    try:
        res = dev.write(bytes(buf))
        if res < 0:
            print(f"ERROR: Operation failed: {res}")
            return res
        return dev.read(33)
    except IOError as e:
        print(f"ERROR: Operation failed: {e}")
        return -1

def show_help():
    print("Usage: script.py [options]")
    print("Options:")
    print("  -e              Enumerate HID devices")
    print("  -i              Enable all outputs")
    print("  -I              Disable all outputs")
    print("  -d              Enable all options")
    print("  -c [channel]    Set input channel (mic, hiz, line, mic_hiz, mute)")
    print("  -M              Enable monitor")
    print("  -m              Disable monitor")
    print("  -l [volume]     Set input left volume (0-127)")
    print("  -r [volume]     Set input right volume (0-127)")
    print("  -L [volume]     Set output left volume (0-145)")
    print("  -R [volume]     Set output right volume (0-145)")
    print("  -h              Show this help message")


def main():
    # Valores de opciones
    input_l, input_r = 86, 86
    output_l, output_r = 145, 145
    monitor, input_mute = False, False
    input_channel = 0x8  # MIC: 0x1, HIZ: 0x2, LINE: 0x4, MIC_HIZ: 0x8, MUTE: 0xc1

    do_e, do_i, do_I ,do_c, do_m, do_l, do_r, do_L, do_R = False,False, False, False, False, False, False, False, False

    # Parsear argumentos
      # Parsear argumentos
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "eidc:Mml:r:L:R:Ih")
    except getopt.GetoptError as err:
        print(f"ERROR: {err}")
        show_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-e':
            do_e = True
        elif opt == '-i':
            do_i = True
        elif opt == '-I':
            do_I = True
        elif opt == '-d':
            do_i = do_c = do_m = do_l = do_r = do_L = do_R = True
        elif opt == '-c':
            do_c = True
            if arg == 'mic':
                input_channel = 0x1
            elif arg == 'hiz':
                input_channel = 0x2
            elif arg == 'line':
                input_channel = 0x4
            elif arg == 'mic_hiz':
                input_channel = 0x8
            elif arg == 'mute':
                input_channel = 0xc1
            else:
                do_c = False
        elif opt == '-M':
            do_m = True
            monitor = True
        elif opt == '-m':
            do_m = True
        elif opt == '-l':
            do_l = True
            input_l = max_val(min_val(int(arg), 127), 0)
        elif opt == '-r':
            do_r = True
            input_r = max_val(min_val(int(arg), 127), 0)
        elif opt == '-L':
            do_L = True
            output_l = max_val(min_val(int(arg), 145), 0)
        elif opt == '-R':
            do_R = True
            output_r = max_val(min_val(int(arg), 145), 0)
        elif opt =='-h':
            show_help()

    # Conectar al dispositivo
    try:
        hiddev = hid.device()

        if do_e:
            enumerate_hid()

        if do_i or do_c or do_m or do_l or do_r or do_L or do_R or do_I:
            hiddev.open(VENDOR_ID, PRODUCT_ID)
            if do_i:
                print("  Enable all out")
                send(hiddev, 0x1a, 0x00)
            if do_I:
                print("  Disable all out")
                send(hiddev, 0x1a, 0x01)  # Comando adicional para desactivar auriculares
            if do_c:
                print(f"  Set input channel: {input_channel}")
                send(hiddev, 0x2a, input_channel)
            if do_m:
                print(f"  Set monitor: {'enable' if monitor else 'disable'}")
                send(hiddev, 0x2c, 0x05 if monitor else 0x01)
            if do_l:
                #print(f"  Set input left volume: {input_l}")
                send(hiddev, 0x1c, input_l + 104)  # 104 - valor mínimo
            if do_r:
                #print(f"  Set input right volume: {input_r}")
                send(hiddev, 0x1e, input_r + 104)  # 104 - valor mínimo
            if do_L:
                #print(f"  Set output left volume: {output_l}")
                send(hiddev, 0x07, output_l + 110)  # 110 - valor mínimo
            if do_R:
                #print(f"  Set output right volume: {output_r}")
                send(hiddev, 0x09, output_r + 110)  # 110 - valor mínimo
            hiddev.close()

    except IOError as e:
        print(f"Unable to open hid device: {e}")

if __name__ == "__main__":
    main()
