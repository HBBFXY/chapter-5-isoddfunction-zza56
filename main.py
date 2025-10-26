# 在此文件中实现 isOdd 函数
def isOdd(n):
    # 检查是否为整数类型且排除布尔类型
    if isinstance(n, int) and not isinstance(n, bool):
        # 判断是否为奇数
        return n % 2 == 1
    return False
    
