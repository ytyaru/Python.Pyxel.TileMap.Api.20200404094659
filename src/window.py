#!/usr/bin/env python3
# coding: utf8
import pyxel
def update(): pass
def draw(): pyxel.bltm(0, 0, 0, 0, 0, 32, 32)
pyxel.init(32, 32, caption='TileMap API Test')
pyxel.image(0).set(0, 0, [
    "3333333333333333",
    "333333333333a333",
    "33333b33333a7a33",
    "33333b333333a333",
    "33333b333333b333",
    "3b333333333bbb33",
    "3b3333333333b333",
    "3333333333333333",
    "4444444400000000",
    "4444444400000000",
    "44444d4400000000",
    "4444444400000000",
    "4444444400000000",
    "4444444400000000",
    "4d44444400000000",
    "4444444400000000",
])
pyxel.tilemap(0).refimg = 0
pyxel.tilemap(0).set(0, 0, [
    '001000000000',
    '000001000000',
    '000000001000',
    '000000000001'
])
pyxel.run(update, draw)

#print(dir(pyxel.tilemap))
#pyxel.tilemap(0)
#pyxel.tilemap(0).set(0, 0, [['000', '001'], ['000', '001']])
#pyxel.tilemap(0).set(0, 0, ['000', '001', '000', '001'])
#pyxel.tilemap(0, refimg=0).set(0, 0, [0, 1])
#map0 = pyxel.tilemap(0).set(0, 0, [0, 1])
#print(dir(map0))
