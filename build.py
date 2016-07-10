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


import collections
import os
import shutil
import subprocess
import tempfile
import xml.sax.handler
import xml.sax.saxutils
import xml.sax.xmlreader


def transform(source, layers):
    filename_layers_visible = collections.defaultdict(lambda: [False] * len(layers))
    for index, layer in enumerate(layers):
        if layer.png_fn:
            filename_layers_visible[layer.png_fn][index] = True

    with tempfile.TemporaryDirectory() as dirname:
        rotated = os.path.join(dirname, 'rotated.svg')
        cut_ = os.path.join(dirname, 'cut.svg')

        rotate(source, layers, rotated)
        for destination, layers_visible in filename_layers_visible.items():
            cut(rotated, layers_visible, cut_)
            pngize(cut_, destination)


def rotate(source, layers, destination):
    with open(destination, 'wb') as destination_file:
        parser = xml.sax.make_parser()
        parser.setContentHandler(RotatedRootGroupsXMLGenerator(layers, destination_file))
        parser.setFeature(xml.sax.handler.feature_namespaces, True)
        parser.parse(source)


def cut(source, layers_visible, destination):
    args = ['inkscape', '--verb=LayerHideAll'] + ['--verb=LayerPrev'] * len(layers_visible)
    for visible in layers_visible:
        if visible:
            args.append('--verb=LayerToggleHide')
        args.append('--verb=LayerNext')
    args += ['--verb=FitCanvasToDrawing', '--verb=FileSave', '--verb=FileQuit', destination]
    shutil.copy2(source, destination)
    subprocess.check_call(args)


def pngize(source, destination):
    subprocess.check_call(['inkscape', '--export-png={}'.format(destination), source])


class Transformations:

    def __init__(self, png_fn=None, rotation=0):
        self.png_fn = png_fn
        self.rotation = rotation


class RotatedRootGroupsXMLGenerator(xml.sax.saxutils.XMLGenerator):

    ELEMENT_NAME = 'http://www.w3.org/2000/svg', 'g'

    ATTRIBUTE_NAME = (None, 'transform')

    ATTRIBUTE_QNAME = 'transform'

    ATTRIBUTE_VALUE = 'rotate({0.rotation})'

    def __init__(self, root_groups, out):
        super().__init__(out, 'utf-8', short_empty_elements=True)
        self.root_group_index = -1
        self.groups_depth = 0
        self.root_groups = root_groups

    @classmethod
    def is_group(cls, name):
        return name == cls.ELEMENT_NAME

    @classmethod
    def make_attributes(cls, group):
        value = cls.ATTRIBUTE_VALUE.format(group)
        attrs = {cls.ATTRIBUTE_NAME: value}
        qnames = {cls.ATTRIBUTE_NAME: cls.ATTRIBUTE_QNAME}
        return xml.sax.xmlreader.AttributesNSImpl(attrs, qnames)

    def startElementNS(self, name, qname, attrs):
        super().startElementNS(name, qname, attrs)
        if self.is_group(name):
            if not self.groups_depth:
                self.root_group_index += 1
                attrs_ = self.make_attributes(self.root_groups[self.root_group_index])
                super().startElementNS(name, qname, attrs_)
            self.groups_depth += 1

    def endElementNS(self, name, qname):
        if self.is_group(name):
            self.groups_depth -= 1
            if not self.groups_depth:
                super().endElementNS(name, qname)
        super().endElementNS(name, qname)


if __name__ == '__main__':
    alitrunk = Transformations('body.png')
    alitrunk_stripes = Transformations('body.png')
    antenna_left = Transformations()
    antenna_right = Transformations('antenna.png', -40)
    eye_left = Transformations('body.png')
    eye_right = Transformations('body.png')
    femur_left_hind = Transformations()
    femur_left_middle = Transformations()
    femur_left_front = Transformations()
    femur_right_front = Transformations()
    femur_right_hind = Transformations()
    femur_right_middle = Transformations('femur.png', -58)
    head = Transformations('body.png')
    gaster = Transformations('body.png')
    tibia_left_hind = Transformations('tibia_left_hind.png')
    tibia_left_middle = Transformations('tibia_left_middle.png')
    tibia_left_front = Transformations()
    tibia_right_front = Transformations('tibia_front.png', -135)
    tibia_right_hind = Transformations('tibia_right_hind.png')
    tibia_right_middle = Transformations('tibia_right_middle.png')

    transform('ant.svg', [
        femur_right_middle,
        tibia_right_middle,
        femur_right_hind,
        tibia_right_hind,
        antenna_right,
        antenna_left,
        gaster,
        femur_left_middle,
        tibia_left_middle,
        femur_left_hind,
        tibia_left_hind,
        femur_right_front,
        tibia_right_front,
        alitrunk,
        alitrunk_stripes,
        eye_right,head,
        eye_left,
        femur_left_front,
        tibia_left_front])
