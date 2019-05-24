# str="123"
# if [ -n $1 ];then
#     echo "哈哈哈"
# else
#     echo "呵呵呵"
# fi

# a=10
# b=20
# echo $((a+b))

# c="123456789"
# echo ${c:3:3}
# echo ${#c}

# echo "\033[31m => 输入您的姓名 \033[0m"
# read m
# echo "打印 =>" $m
# exit 0

# read -p "Enter your name: " name
# echo "hello $name"
# exit 0

read  -s  -p "Enter your password:" pass
echo "your password is $pass"
exit 0