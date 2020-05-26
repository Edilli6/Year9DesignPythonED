 1. # Memory Puzzle

  2. # By Al Sweigart al@inventwithpython.com

  3. # http://inventwithpython.com/pygame

  4. # Released under a "Simplified BSD" license

  5.

  6. import random, pygame, sys

  7. from pygame.locals import *

  8.

  9. FPS = 30 # frames per second, the general speed of the program

 10. WINDOWWIDTH = 640 # size of window's width in pixels

 11. WINDOWHEIGHT = 480 # size of windows' height in pixels

 12. REVEALSPEED = 8 # speed boxes' sliding reveals and covers

 13. BOXSIZE = 40 # size of box height & width in pixels

 14. GAPSIZE = 10 # size of gap between boxes in pixels

 15. BOARDWIDTH = 10 # number of columns of icons

 16. BOARDHEIGHT = 7 # number of rows of icons

 17. assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'

 18. XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)

 19. YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

 20.

 21. #            R    G    B

 22. GRAY     = (100, 100, 100)

 23. NAVYBLUE = ( 60,  60, 100)

 24. WHITE    = (255, 255, 255)

 25. RED      = (255,   0,   0)

 26. GREEN    = (  0, 255,   0)

 27. BLUE     = (  0,   0, 255)

 28. YELLOW   = (255, 255,   0)

 29. ORANGE   = (255, 128,   0)

 30. PURPLE   = (255,   0, 255)

 31. CYAN     = (  0, 255, 255)

 32.

 33. BGCOLOR = NAVYBLUE

 34. LIGHTBGCOLOR = GRAY

 35. BOXCOLOR = WHITE

 36. HIGHLIGHTCOLOR = BLUE

 37.

 38. DONUT = 'donut'

 39. SQUARE = 'square'

 40. DIAMOND = 'diamond'

 41. LINES = 'lines'

 42. OVAL = 'oval'

 43.

 44. ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)

 45. ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)

 46. assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."

 47.

 48. def main():

 49.     global FPSCLOCK, DISPLAYSURF

 50.     pygame.init()

 51.     FPSCLOCK = pygame.time.Clock()

 52.     DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

 53.

 54.     mousex = 0 # used to store x coordinate of mouse event

 55.     mousey = 0 # used to store y coordinate of mouse event

 56.     pygame.display.set_caption('Memory Game')

 57.

 58.     mainBoard = getRandomizedBoard()

 59.     revealedBoxes = generateRevealedBoxesData(False)

 60.

 61.     firstSelection = None # stores the (x, y) of the first box clicked.

 62.

 63.     DISPLAYSURF.fill(BGCOLOR)

 64.     startGameAnimation(mainBoard)

 65.

 66.     while True: # main game loop

 67.         mouseClicked = False

 68.

 69.         DISPLAYSURF.fill(BGCOLOR) # drawing the window

 70.         drawBoard(mainBoard, revealedBoxes)

 71.

 72.         for event in pygame.event.get(): # event handling loop

 73.             if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):

 74.                 pygame.quit()

 75.                 sys.exit()

 76.             elif event.type == MOUSEMOTION:

 77.                 mousex, mousey = event.pos

 78.             elif event.type == MOUSEBUTTONUP:

 79.                 mousex, mousey = event.pos

 80.                 mouseClicked = True

 81.

 82.         boxx, boxy = getBoxAtPixel(mousex, mousey)

 83.         if boxx != None and boxy != None:

 84.             # The mouse is currently over a box.

 85.             if not revealedBoxes[boxx][boxy]:

 86.                drawHighlightBox(boxx, boxy)

 87.             if not revealedBoxes[boxx][boxy] and mouseClicked:

 88.                 revealBoxesAnimation(mainBoard, [(boxx, boxy)])

 89.                 revealedBoxes[boxx][boxy] = True # set the box as "revealed"

 90.                 if firstSelection == None: # the current box was the first box clicked

 91.                     firstSelection = (boxx, boxy)

 92.                 else: # the current box was the second box clicked

 93.                     # Check if there is a match between the two icons.

 94.                     icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])

 95.                     icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)

 96.

 97.                     if icon1shape != icon2shape or icon1color != icon2color:

 98.                         # Icons don't match. Re-cover up both selections.

 99.                         pygame.time.wait(1000) # 1000 milliseconds = 1 sec

100.                         coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])

101.                         revealedBoxes[firstSelection[0]][firstSelection [1]] = False

102.                         revealedBoxes[boxx][boxy] = False

103.                     elif hasWon(revealedBoxes): # check if all pairs found

104.                         gameWonAnimation(mainBoard)

105.                         pygame.time.wait(2000)

106.

107.                         # Reset the board

108.                         mainBoard = getRandomizedBoard()

109.                         revealedBoxes = generateRevealedBoxesData(False)

110.

111.                         # Show the fully unrevealed board for a second.

112.                         drawBoard(mainBoard, revealedBoxes)

113.                         pygame.display.update()

114.                         pygame.time.wait(1000)

115.

116.                         # Replay the start game animation.

117.                         startGameAnimation(mainBoard)           

118.                     firstSelection = None # reset firstSelection variable

119.

120.         # Redraw the screen and wait a clock tick.

121.         pygame.display.update()

122.         FPSCLOCK.tick(FPS)

123.

124.

125. def generateRevealedBoxesData(val):

126.     revealedBoxes = []

127.     for i in range(BOARDWIDTH):

128.         revealedBoxes.append([val] * BOARDHEIGHT)

129.     return revealedBoxes

130.

131.

132. def getRandomizedBoard():

133.     # Get a list of every possible shape in every possible color.

134.     icons = []

135.     for color in ALLCOLORS:

136.         for shape in ALLSHAPES:

137.             icons.append( (shape, color) )

138.

139.     random.shuffle(icons) # randomize the order of the icons list

140.     numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) # calculate how many icons are needed

141.     icons = icons[:numIconsUsed] * 2 # make two of each

142.     random.shuffle(icons)

143.

144.     # Create the board data structure, with randomly placed icons.

145.     board = []

146.     for x in range(BOARDWIDTH):

147.         column = []

148.         for y in range(BOARDHEIGHT):

149.             column.append(icons[0])

150.             del icons[0] # remove the icons as we assign them

151.         board.append(column)

152.     return board

153.

154.

155. def splitIntoGroupsOf(groupSize, theList):

156.     # splits a list into a list of lists, where the inner lists have at

157.     # most groupSize number of items.

158.     result = []

159.     for i in range(0, len(theList), groupSize):

160.         result.append(theList[i:i + groupSize])

161.     return result

162.

163.

164. def leftTopCoordsOfBox(boxx, boxy):

165.     # Convert board coordinates to pixel coordinates

166.     left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN

167.     top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN

168.     return (left, top)

169.

170.

171. def getBoxAtPixel(x, y):

172.     for boxx in range(BOARDWIDTH):

173.         for boxy in range(BOARDHEIGHT):

174.             left, top = leftTopCoordsOfBox(boxx, boxy)

175.             boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)

176.             if boxRect.collidepoint(x, y):

177.                 return (boxx, boxy)

178.     return (None, None)

179.

180.

181. def drawIcon(shape, color, boxx, boxy):

182.     quarter = int(BOXSIZE * 0.25) # syntactic sugar

183.     half =    int(BOXSIZE * 0.5)  # syntactic sugar

184.

185.     left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from board coords

186.     # Draw the shapes

187.     if shape == DONUT:

188.         pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)

189.         pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)

190.     elif shape == SQUARE:

191.         pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))

192.     elif shape == DIAMOND:

193.         pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))

194.     elif shape == LINES:

195.         for i in range(0, BOXSIZE, 4):

196.             pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))

197.             pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))

198.     elif shape == OVAL:

199.         pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))

200.

201.

202. def getShapeAndColor(board, boxx, boxy):

203.     # shape value for x, y spot is stored in board[x][y][0]

204.     # color value for x, y spot is stored in board[x][y][1]

205.     return board[boxx][boxy][0], board[boxx][boxy][1]

206.

207.

208. def drawBoxCovers(board, boxes, coverage):

209.     # Draws boxes being covered/revealed. "boxes" is a list

210.     # of two-item lists, which have the x & y spot of the box.

211.     for box in boxes:

212.         left, top = leftTopCoordsOfBox(box[0], box[1])

213.         pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))

214.         shape, color = getShapeAndColor(board, box[0], box[1])

215.         drawIcon(shape, color, box[0], box[1])

216.         if coverage > 0: # only draw the cover if there is an coverage

217.             pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))

218.     pygame.display.update()

219.     FPSCLOCK.tick(FPS)

220.

221.

222. def revealBoxesAnimation(board, boxesToReveal):

223.     # Do the "box reveal" animation.

224.     for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, - REVEALSPEED):

225.         drawBoxCovers(board, boxesToReveal, coverage)

226.

227.

228. def coverBoxesAnimation(board, boxesToCover):

229.     # Do the "box cover" animation.

230.     for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):

231.         drawBoxCovers(board, boxesToCover, coverage)

232.

233.

234. def drawBoard(board, revealed):

235.     # Draws all of the boxes in their covered or revealed state.

236.     for boxx in range(BOARDWIDTH):

237.         for boxy in range(BOARDHEIGHT):

238.             left, top = leftTopCoordsOfBox(boxx, boxy)

239.             if not revealed[boxx][boxy]:

240.                 # Draw a covered box.

241.                 pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))

242.             else:

243.                 # Draw the (revealed) icon.

244.                 shape, color = getShapeAndColor(board, boxx, boxy)

245.                 drawIcon(shape, color, boxx, boxy)

246.

247.

248. def drawHighlightBox(boxx, boxy):

249.     left, top = leftTopCoordsOfBox(boxx, boxy)

250.     pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)

251.

252.

253. def startGameAnimation(board):

254.     # Randomly reveal the boxes 8 at a time.

255.     coveredBoxes = generateRevealedBoxesData(False)

256.     boxes = []

257.     for x in range(BOARDWIDTH):

258.         for y in range(BOARDHEIGHT):

259.             boxes.append( (x, y) )

260.     random.shuffle(boxes)

261.     boxGroups = splitIntoGroupsOf(8, boxes)

262.

263.     drawBoard(board, coveredBoxes)

264.     for boxGroup in boxGroups:

265.         revealBoxesAnimation(board, boxGroup)

266.         coverBoxesAnimation(board, boxGroup)

267.

268.

269. def gameWonAnimation(board):

270.     # flash the background color when the player has won

271.     coveredBoxes = generateRevealedBoxesData(True)

272.     color1 = LIGHTBGCOLOR

273.     color2 = BGCOLOR

274.

275.     for i in range(13):

276.         color1, color2 = color2, color1 # swap colors

277.         DISPLAYSURF.fill(color1)

278.         drawBoard(board, coveredBoxes)

279.         pygame.display.update()

280.         pygame.time.wait(300)

281.

282.

283. def hasWon(revealedBoxes):

284.     # Returns True if all the boxes have been revealed, otherwise False

285.     for i in revealedBoxes:

286.         if False in i:

287.             return False # return False if any boxes are covered.

288.     return True

289.

290.

291. if __name__ == '__main__':

292.     main()