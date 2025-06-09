from typing import List

class Solution: 
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:  # untuk menangani list kosong
            return 0

        min_price = float('inf')  #inisialisasi min_price dengan nilai tak terbatas
        max_profit = 0            #inisialisasi max_profit dengan 0

        # melakukan iterasi melalui setiap harga dalam daftar
        for price in prices:
            # Jika harga saat ini lebih rendah dari min_price yang tercatat,
            # perbarui min_price. Ini adalah hari terbaik untuk membeli sejauh ini.
            if price < min_price:
                min_price = price
            # Jika harga saat ini lebih tinggi dari min_price,
            # hitung potensi keuntungan dan perbarui max_profit jika lebih besar.
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

if __name__ == "__main__":
    s = Solution()

