# %r 根据变量格式确定输出，是字符串就自动带引号是数字就不带引号等等,万用型
formatter = "%r %r %r %r"

# 注意括号的应用
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# 字符里面带字符
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
