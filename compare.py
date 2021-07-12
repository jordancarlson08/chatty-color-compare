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
colorPalette = str(input("Enter color palette to test against: "))
print("")
testColor = '#' + str(input("Enter hex to compare: #"))

grays = {
	"gray_50":"#F8FAFC",
    "gray_100":"#F1F5F9",
    "gray_200":"#E2E8F0",
    "gray_300":"#CFD8E3",
    "gray_400":"#B8C3D1",
    "gray_500":"#97A6BA",
    "gray_600":"#7A899F",
    "gray_700":"#52627A",
    "gray_800":"#3D495C",
    "gray_900":"#27303F",
}

brands = {
	"brand_50":"#F0FFFB",
    "brand_100":"#E1FCF7",
    "brand_200":"#B0F0E2",
    "brand_300":"#80E0CE",
    "brand_400":"#00CFB4",
    "brand_500":"#00A896",
    "brand_600":"#008177",
    "brand_700":"#006961",
    "brand_800":"#00504A",
    "brand_900":"#002825",
}

blues = {
	"blue_50":"#F7FBFF",
    "blue_100":"#EBF8FF",
    "blue_200":"#C0E6FA",
    "blue_300":"#9CCEFF",
    "blue_400":"#69A1F0",
    "blue_500":"#357FE8",
    "blue_600":"#255DAF",
    "blue_700":"#1B4685",
    "blue_800":"#112E5A",
    "blue_900":"#09172D",
}

yellows = {
    "yellow_50":"#FCFAF3",
    "yellow_100":"#FFF9DE",
    "yellow_200":"#FFEEA3",
    "yellow_300":"#FFE67B",
    "yellow_400":"#F9D22D",
    "yellow_500":"#E2B330",
    "yellow_600":"#C78516",
    "yellow_700":"#8C5C0B",
    "yellow_800":"#503300",
    "yellow_900":"#281A00",
}

pinks = {
	"pink_50":"#FFF5F5",
    "pink_100":"#FCEDEE",
    "pink_200":"#FCCEDD",
    "pink_300":"#FCB4D0",
    "pink_400":"#EA73B4",
    "pink_500":"#CA3975",
    "pink_600":"#991658",
    "pink_700":"#7A1447",
    "pink_800":"#5A1135",
    "pink_900":"#2D091B",
}

reds = {
	"red_50":"#FFF4EE",
    "red_100":"#FFE1D4",
    "red_200":"#FFB69C",
    "red_300":"#FF9473",
    "red_400":"#FF534A",
    "red_500":"#E02222",
    "red_600":"#AD0B0B",
    "red_700":"#840E0E",
    "red_800":"#5A1111",
    "red_900":"#2D0909",
}

colors = {
	"gray": grays,
	"brand": brands,
	"blue": blues,
	"yellow": yellows,
	"pink": pinks,
	"red": reds,
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