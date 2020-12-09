#!/usr/bin/env bash

BOXNAME=${1?Error: no name given}
YVAL=${2?Error: no name given}
XVAL=${3?Error: no name given}



rosrun gazebo_ros spawn_model -file boxurdf.urdf -urdf -model $BOXNAME -y $YVAL -x $XVAL -z 5.0