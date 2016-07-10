# Copyright 2016 RunSugarRun authors.
# See the AUTHORS file found in the top-level directory of this
# distribution and at https://github.com/kosova-holy/Ant.
#
# Licensed under the MIT License. See the LICENSE file found in the
# top-level directory of this distribution and at
# https://github.com/kosova-holy/Ant. No part of RunSugarRun, including
# this file, may be copied, modified, propagated, or distributed except
# according to the terms contained in the LICENSE file.
#
# This document provides a complete list of all the contributors that
# have ever contributed to RunSugarRun in order to give them credit.


import pickle

import cocos

import ant
import skin


class Actors(cocos.layer.Layer):

    def __init__(self):
        super().__init__()
        self.add(cocos.sprite.Sprite('background.jpg', anchor=(0, 0)))
        ant_ = cocos.skeleton.BitmapSkin(ant.skeleton, skin.skin)
        ant_.scale = 0.1
        ant_.width = 56
        ant_.height = 77
        ant_.position = (965, 0)
        ant_.velocity = (-20, 20)
        ant_.do(
            cocos.actions.Repeat(cocos.skeleton.Animate(pickle.load(open('ant.anim', 'rb')))) |
            cocos.actions.BoundedMove(965, 705))
        self.add(ant_)

cocos.director.director.init(width=965, height=705)
cocos.director.director.run(cocos.scene.Scene(Actors()))
