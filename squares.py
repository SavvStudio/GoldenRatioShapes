svg = open("squares.svg", "w")
svg.write('<?xml version="1.0" encoding="UTF-8" ?>')
svg.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1">')

goldenratio = 1.618

width = int(input("Starting width: "))
squareCount = int(input("Squares to generate: "))

for i in range(1,squareCount+1):
    svg.write('<rect x="0" y="0" width="'+ str(width) + '" height="' + str(width) + '" fill="none" stroke-width="4" stroke="black" />')
    width = width * goldenratio

svg.write('</svg>')
svg.close()
