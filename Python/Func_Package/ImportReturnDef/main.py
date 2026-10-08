#mengimport variable dari layanan_ai dan mengolahnya

import layanan_ai

biaya_in = layanan_ai.biaya_input(2000)

biaya_out = layanan_ai.biaya_output(1000)

grand_total = layanan_ai.total_biaya(biaya_in, biaya_out)

print(biaya_in)
print(biaya_out)
print(grand_total)
