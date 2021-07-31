
# 异常

# 使用try...except...捕获异常
try:
    a = 1 / 0
except Exception as e:
    print("异常捕获信息 : ", e)



# 自定义异常
# 通过继承Exception实现自定义的异常
class myError(Exception):
    pass

# 使用raise抛出自定义异常, 
# 格式: raise 异常名称('异常描述')
# raise myError( "异常" )



# 
if __name__ == "__main__":
    pass





