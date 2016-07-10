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

from cocos.skeleton import Bone, Skeleton

def Point2(*args): return args

root_bone = Bone('body', 480, 180.0, Point2(0.00, -157.00)).add(
    Bone('right_antenna', 120, 320.0, Point2(1.00, -477.00))
).add(
    Bone('left_antenna', 120, 317.0, Point2(-38.00, -436.00))
).add(
    Bone('front_left_femur', 90, 301.0, Point2(-31.00, -245.00))    .add(
        Bone('front_left_tibia', 130, 284.0, Point2(1.00, -89.00))
)
).add(
    Bone('front_right_femur', 90, 122.0, Point2(83.00, -244.00))    .add(
        Bone('front_right_tibia', 130, 644.0, Point2(1.00, -89.00))
)
).add(
    Bone('middle_left_femur', 90, 238.0, Point2(-25.00, -18.00))    .add(
        Bone('middle_left_tibia', 160, -57.00000000000001, Point2(-1.00, -91.00))
)
).add(
    Bone('middle_right_femur', 90, 122.0, Point2(17.00, -23.00))    .add(
        Bone('middle_right_tibia', 160, 58.00000000000001, Point2(1.00, -90.00))
)
).add(
    Bone('hind_left_femur', 90, 238.0, Point2(-131.00, -6.00))    .add(
        Bone('hind_left_tibia', 160, -59.00000000000001, Point2(0.00, -90.00))
)
).add(
    Bone('hind_right_femur', 90, 122.0, Point2(-87.00, -27.00))    .add(
        Bone('hind_right_tibia', 160, 58, Point2(0.00, -89.00))
)
)


skeleton = Skeleton( root_bone )
