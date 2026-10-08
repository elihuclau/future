#data utama untuk di olah kembali di modul main.py

def biaya_input(token_input):
    return token_input * 0.0015

def biaya_output(token_output):
    return token_output * 0.0050

def total_biaya(biaya_in, biaya_out):
    return biaya_in + biaya_out
