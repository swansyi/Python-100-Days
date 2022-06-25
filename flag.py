"""
用Python的turtle模块绘制国旗
"""
import turtle


def draw_rectangle(x, y, width, height):
    """绘制矩形"""
    turtle.goto(x, y)
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)   #forward前进 backward后退
        turtle.left(90)     #rotation
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw_star(x, y, radius):
    """绘制五角星"""
    turtle.setpos(x, y)     #前往位置
    pos1 = turtle.pos()     #获得位置
    turtle.circle(-radius, 72)  #画圆 顺时针正(radius半径, extent圆心角度数=None, steps起点到重点线段数=None)
    pos2 = turtle.pos()
    turtle.circle(-radius, 72)
    pos3 = turtle.pos()
    turtle.circle(-radius, 72)
    pos4 = turtle.pos()
    turtle.circle(-radius, 72)
    pos5 = turtle.pos()
    turtle.color('yellow', 'yellow')
    turtle.begin_fill()
    turtle.goto(pos3)   #连线画五角星
    turtle.goto(pos1)
    turtle.goto(pos4)
    turtle.goto(pos2)
    turtle.goto(pos5)
    turtle.end_fill()


def main():
    """主程序"""
    turtle.speed(8) #画图速度
    turtle.penup()  #turtle.penup()：过程路径不显示 pendown()：过程路径全显示
    x, y = -270, -180   #初始位置 画布中心为0
    # 画国旗主体
    width, height = 540, 360
    draw_rectangle(x, y, width, height)
    # 画大星星
    pice = 22
    center_x, center_y = x + 5 * pice, y + height - pice * 5
    turtle.goto(center_x, center_y)
    turtle.left(90)
    turtle.forward(pice * 3)
    turtle.right(90)
    draw_star(turtle.xcor(), turtle.ycor(), pice * 3)   #xcor() ycor() xy坐标
    x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]
    # 画小星星
    for x_pos, y_pos in zip(x_poses, y_poses):
        turtle.goto(x + x_pos * pice, y + height - y_pos * pice)
        turtle.left(turtle.towards(center_x, center_y) - turtle.heading())  #towards：目标方向  heading：朝向
        turtle.forward(pice)
        turtle.right(90)
        draw_star(turtle.xcor(), turtle.ycor(), pice)
    # 隐藏海龟
    turtle.ht()
    # 显示绘图窗口 运行完成后等待进一步的指令，删除后窗口运行后自动关闭
    turtle.mainloop()


if __name__ == '__main__':
    main()