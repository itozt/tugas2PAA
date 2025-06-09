from typing import List 

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # base case
        if n == 0:
            return 0
        if n == 1:
            return 1 # Untuk n = 1, hanya ada 1 cara: (1 langkah).
        if n == 2:
            return 2 # Untuk n = 2, ada 2 cara: (1 langkah + 1 langkah) atau (2 langkah).

        # Pada awal loop (ketika i=3), ini akan mewakili jumlah cara untuk langkah 1, yaitu 1.
        two_steps_before = 1

        # Pada awal loop (ketika i=3), ini akan mewakili jumlah cara untuk langkah 2, yaitu 2.
        one_step_before = 2

        for i in range(3, n + 1):
            # Jumlah cara untuk mencapai langkah 'i' adalah hasil penjumlahan jumlah cara dari langkah (i-1) dan jumlah cara dari langkah (i-2).
            current_ways = one_step_before + two_steps_before

            # Perbarui variabel untuk iterasi berikutnya:
            # Nilai yang sebelumnya ada di 'one_step_before' kini menjadi 'two_steps_before' untuk iterasi selanjutnya.
            two_steps_before = one_step_before

            # Nilai 'current_ways' yang baru dihitung kini menjadi 'one_step_before' untuk iterasi selanjutnya.
            one_step_before = current_ways

        # Setelah loop selesai, variabel 'one_step_before' akan berisi total jumlah cara untuk mencapai langkah 'n'.
        return one_step_before
