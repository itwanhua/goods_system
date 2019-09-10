#!/etc/bin/python3
# -*- coding: utf-8 -*-

import sys
import goods
import good_operation 


def menu():
    print("*"*30 + "商品信息管理系统" + "*"*30)
    print("1.增加商品  2.查询商品  3.修改商品  4.删除商品  5.退出系统")

def main():
    menu()
    while True:
        op = input("请输入功能菜单：")
        
        if op == "1":
            name = input("请输入商品名称：")
            try:
                price = float(input("请输入商品单价："))
                num = int(input("请输入商品数量："))
            except:
                print("输入有误！")
                continue
            g = goods.good()
            g.set_gname(name)
            g.set_gprice(price)
            g.set_gnum(num)
            good_operation.add_good(g)
            print("商品添加成功！")


        elif op == "2":
            print("*"*30 + "商品查询菜单" + "*"*30)
            print("1.查询所有商品  2.通过商品ID查询  3.通过商品名称查询")
            opf = input("请输入查询菜单：")
            if opf == "1":
                rows = good_operation.get_all()
                print(rows)

            elif opf == "2":
                try:
                    gid = int(input("请输入商品ID："))
                except:
                    print("输入有误！")
                    continue
                g = goods.good()
                g.set_gid(gid)
                row = good_operation.get_byid(s)
                print(row)

            elif opf == "3":
                name = input("请输入商品名称：")
                g = goods.good()
                g.set_gname(name)
                row = good_operation(g)
                print(row)

            else:
                print("输入有误！")

        elif op == "3":
            try:
                gid = int(input("请输入商品ID："))
                name = input("请输入商品名称：")
                price = float(input("请输入商品单价："))
                num = int(input("请输入商品数量："))
            except:
                print("输入有误！")
                continue
            g = goods.good()
            g.set_gname(name)
            g.set_gprice(price)
            g.set_gnum(num)
            good_operation.update_good(g)
            print("商品增加成功！")

        elif op == "4":
            try:
                gid = int(input("请输入商品ID："))
            except:
                print("输入有误！")
                continue
            g = goods.good()
            g.set_gid(gid)
            good_operation.delete_good(g)
            print("商品删除成功！")

        elif op == "5":
            sys.exit()

        else:
            print("输入有误！")
            continue


if __name__ == "__main__":
    main()
