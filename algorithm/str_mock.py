'''
给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求 不使用 乘法、除法和取余运算。

整数除法应该向零截断，也就是截去（truncate）其小数部分。例如，8.345 将被截断为 8 ，-2.7335 将被截断至 -2 。

返回被除数 dividend 除以除数 divisor 得到的 商 。

注意：假设我们的环境只能存储 32 位 有符号整数，其数值范围是 [−231,  231 − 1] 。本题中，如果商 严格大于 231 − 1 ，则返回 231 − 1 ；如果商 严格小于 -231 ，则返回 -231 。
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        '''
        利用位运算，将除法变为逆乘法
        dividend/divisor = 商 ... mod
        dividend  <==> divisor*商 + mod <==> divisor*(1...0...) + mod
        从高位而不是低位，因为在递推中高位唯一
        '''
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        a,b = abs(dividend),abs(divisor)
        count,res = 31, 0
        for i in range(count+1):
            if b << count <= a:
                res += 1 << count
                a -= b << count
            count -= 1
        return res if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0) else -res