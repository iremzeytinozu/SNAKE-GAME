##################
### SNAKE GAME ###
##################

# turtle kütüphanesi, Python programlama dilinde grafiksel kullanıcı arayüzü oluşturmak ve temel çizimler yapmak için kullanılan bir modüldür. 
import turtle 
# import time ifadesi, Python'daki time modülünü programınıza dahil eder. 
# Bu modül, zamanla ilgili işlemleri gerçekleştirmenizi sağlayan bir standart kütüphanedir.
import time
# import random ifadesi, Python'daki random modülünü programınıza dahil eder. 
import random


# Turtle ekranını (penceresini) oluşturur. 
# Bu, oyunun görüntülendiği ana ekranı temsil eder.
game_screen = turtle.Screen()
game_screen.title("Snake Game")
game_screen.setup(width = 800, height = 600)
game_screen.bgcolor('lightgreen')
# Ekranın güncellemelerini kapatır.
# Bu, oyunun daha düzenli ve hızlı çalışmasını sağlar.
# tracer(0) fonksiyonu, otomatik güncellemeleri kapatır. 
# update() fonksiyonu çağrılmadığı sürece ekranda herhangi bir değişiklik olmaz.
game_screen.tracer(0)


# turtle.Turtle() fonksiyonu, bir Turtle nesnesi oluşturarak ekranda çizim ve hareket etme işlemlerini gerçekleştirmek için kullanılan bir araçtır.
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.color('grey')
# Yılan başının şeklini daire olarak değiştir
snake_head.shape('circle')
# Bu fonksiyon, Turtle nesnesinin kalemini kaldırarak iz bırakmamasını sağlar.
# Yani, turtle nesnesi hareket ettiğinde iz çizmez.
# Bu, yılan başının sadece görüntüsünü ekranda göstermek için kullanılır.
snake_head.penup()
# Bu fonksiyon, yılan başını belirtilen konuma taşır. 
# Burada (0, 0) koordinatları, yılan başının ekranın ortasına gitmesini sağlar.
# Bu, oyunun başladığı varsayılan başlangıç konumunu temsil edebilir.
snake_head.goto(0,0)
# Bu satır, yılan başının hareket yönünü belirleyen bir özellik olan direction'ı 'stop' olarak ayarlar.
# Bu durumda, yılan başı hareket etmeyecek; yani, başlangıçta duracak.
snake_head.direction = 'stop'


snake_speed = 0.1


bait = turtle.Turtle()
bait.speed(0)
bait.color('orange')
bait.shape('circle')
bait.penup()
bait.goto(0,100)
bait.shapesize(0.8, 0.8)


tail = []


score = 0
score_board = turtle.Turtle()
score_board.speed(0)
score_board.color('white')
score_board.shape('square')
score_board.penup()
score_board.goto(0,250)
# hideturtle(): Bu fonksiyon, Turtle nesnesinin izini (okunu) gizler.
# Yani, turtle nesnesi hareket ettiğinde veya çizim yaptığında iz bırakmaz.
score_board.hideturtle()
score_board.write('Score : {}'.format(score), align='center',font=('Courier', 30,'normal'))


def move():
    if snake_head.direction == 'up':
        y = snake_head.ycor()
        snake_head.sety(y + 10)
    if snake_head.direction == 'down':
        y = snake_head.ycor()
        snake_head.sety(y - 10)
    if snake_head.direction == 'right':
        x = snake_head.xcor()
        snake_head.setx(x + 10)
    if snake_head.direction == 'left':
        x = snake_head.xcor()
        snake_head.setx(x - 10)


def go_up():
    if snake_head.direction != 'down':
        snake_head.direction = 'up'

def down_up():
    if snake_head.direction != 'up':
        snake_head.direction = 'down'

def right_up():
    if snake_head.direction != 'left':
        snake_head.direction = 'right'

def left_up():
    if snake_head.direction != 'right':
        snake_head.direction = 'left'


# Klavye girişlerini dinlemek üzere ekranı hazırlar.
# Yani, klavyeden gelen tuş girişlerini takip etmeye başlar.
game_screen.listen()
# 'Up' (Yukarı) ok tuşuna basıldığında go_up adlı bir fonksiyonun çağrılmasını sağlar. 
# go_up fonksiyonu, yılanın yukarı yönde hareket etmesiyle ilgili işlemleri içerebilir.
game_screen.onkey(go_up, 'Up')
game_screen.onkey(down_up, 'Down')
game_screen.onkey(left_up, 'Left')
game_screen.onkey(right_up, 'Right')


while True:
    game_screen.update()
    
    if snake_head.xcor() > 400 or snake_head.xcor() < -400 or snake_head.ycor() > 300 or snake_head.ycor() < -300:
        time.sleep(1)
        snake_head.goto(0,0)
        snake_head.direction = 'stop'

        for i in tail:
            i.goto(5000,5000)
        
        tail = []
        score = 0
        score_board.clear()
        score_board.write('Score : {}'.format(score), align='center',font=('Courier', 30,'normal'))
        snake_speed = 0.1

    if snake_head.distance(bait) < 20:
        x = random.randint(-200,200)
        y = random.randint(-150,150)
        bait.goto(x,y)
        
        score += 10
        score_board.clear()
        score_board.write('Score : {}'.format(score), align='center',font=('Courier', 30,'normal'))
        snake_speed = snake_speed - 0.005

        add_tail = turtle.Turtle()
        add_tail.speed(0)
        add_tail.shape('circle')
        add_tail.color('grey')
        add_tail.penup()
        tail.append(add_tail)
        
    for i in range(len(tail) - 1, 0,-1):
        x = tail[i-1].xcor()
        y = tail[i-1].ycor()

        tail[i].goto(x,y)

    if len(tail) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        tail[0].goto(x,y)

    move()
    time.sleep(snake_speed)  
