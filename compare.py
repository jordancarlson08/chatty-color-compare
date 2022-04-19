#!/usr/bin/python
import turtle

def diff(h1, h2):
    def hexs_to_ints(s):
        return [int(s[i:i+2], 16) for i in range(1,7,2)]
    return sum(abs(i - j) for i, j in zip(*map(hexs_to_ints, (h1, h2))))

def get_col_name(hex, colors):
    return min([(n,diff(hex,c)) for n,c in colors.items()], key=lambda t: t[1])[0]





# testColor = "#D8E8FF"
print("")
colorPalette = str(input("Enter color palette to test against\ngray, chatty_green, blavender, highlighter, pink, cream, or holiday: "))
print("")
testColor = '#' + str(input("Enter hex to compare: #"))

grays = {
	"gray_50":"#F9FAFC",
    "gray_100":"#EEF1F7",
    "gray_200":"#E3E9F3",
    "gray_300":"#C3CEDF",
    "gray_400":"#94A7BF",
    "gray_500":"#607A94",
    "gray_600":"#3C546A",
    "gray_700":"#263A4B",
    "gray_800":"#1D2D3A",
    "gray_900":"#1A2A36",
}

chatty_green = {
	"chatty_green_50":"#F2FFFD",
    "chatty_green_100":"#D6FCF5",
    "chatty_green_200":"#BCF9ED",
    "chatty_green_300":"#8CF0DD",
    "chatty_green_400":"#64E2CA",
    "chatty_green_500":"#44CFB4",
    "chatty_green_600":"#32B69D",
    "chatty_green_700":"#239580",
    "chatty_green_800":"#186D5D",
    "chatty_green_900":"#0F4239",
}

blavender = {
	"blavender_50":"#F5F8FF",
    "blavender_100":"#E1E8FE",
    "blavender_200":"#CDD9FD",
    "blavender_300":"#A8BCF7",
    "blavender_400":"#88A1EF",
    "blavender_500":"#718DE2",
    "blavender_600":"#5F7BD0",
    "blavender_700":"#4F6AB8",
    "blavender_800":"#40589C",
    "blavender_900":"#33477D",
}

highlighter = {
    "highlighter_50":"#FFFFF6",
    "highlighter_100":"#FEFFDF",
    "highlighter_200":"#FCFFC9",
    "highlighter_300":"#EFFD97",
    "highlighter_400":"#DBF36D",
    "highlighter_500":"#E285D6",
    "highlighter_600":"#C0DC46",
    "highlighter_700":"#799717",
    "highlighter_800":"#50680B",
    "highlighter_900":"#273604",
}

pink = {
    "pink_50":"#FFFAFE",
    "pink_100":"#FFECFD",
    "pink_200":"#FFDEFD",
    "pink_300":"#FDBEF5",
    "pink_400":"#F5A2EA",
    "pink_500":"#E285D6",
    "pink_600":"#C96BBC",
    "pink_700":"#A8549D",
    "pink_800":"#803D77",
    "pink_900":"#572850",
}

cream = {
	"cream_50":"#FFFBF8",
    "cream_100":"#F9EDE5",
    "cream_200":"#F2DFD2",
    "cream_300":"#ECC3A7",
    "cream_400":"#E2A982",
    "cream_500":"#D29063",
    "cream_600":"#BB784A",
    "cream_700":"#9C5F36",
    "cream_800":"#774625",
    "cream_900":"#4F2D16",
}

holiday = {
	"holiday_50":"#FFF7F6",
    "holiday_100":"#FFE4DE",
    "holiday_200":"#FFD0C6",
    "holiday_300":"#FFA491",
    "holiday_400":"#F97E66",
    "holiday_500":"#EB6044",
    "holiday_600":"#CC4428",
    "holiday_700":"#A62E16",
    "holiday_800":"#781D0B",
    "holiday_900":"#471005",
}

colors = {
	"gray": grays,
	"chatty_green": chatty_green,
	"blavender": blavender,
	"highlighter": highlighter,
    "pink": pink,
	"cream": cream,
	"holiday": holiday,
}

selectedPalette = colors[colorPalette]

result = get_col_name(testColor, selectedPalette)

print("")
print(result)
print("")
print("")
print("")

screen = turtle.Screen()
screen.setup(500, 350)


t = turtle.Turtle()
t.speed(100)

t.penup()
t.goto(-225, 125)
t.pendown()

t.color(testColor)
t.fillcolor(testColor)
t.begin_fill()
for _ in range(4):
  t.forward(225)
  t.right(90)
t.end_fill()

t.penup()
t.goto(-112, -150)
t.pendown()
t.write(testColor, align="center",font=("Arial", 24, "bold"))



resultColor = selectedPalette[result]

t.penup()
t.goto(0, 125)
t.pendown()

t.color(resultColor)
t.fillcolor(resultColor)
t.begin_fill()
for _ in range(4):
  t.forward(225)
  t.right(90)
t.end_fill()

t.penup()
t.goto(112, -150)
t.pendown()
t.write(result + ": " + resultColor, align="center", font=("Arial", 24, "bold"))

t.penup()
t.goto(0, 0)
t.pendown()

screen.exitonclick()