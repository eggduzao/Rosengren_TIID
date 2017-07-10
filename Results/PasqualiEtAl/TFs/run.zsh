#!/bin/zsh

#Parameters
inputMatrixR="./ExpMatR.txt"
inputMatrixQ="./ExpMatQ.txt"
outputLocation="./Results/"

# Execution
rgt-viz projection -r $inputMatrixR -q $inputMatrixQ $outputLocation
rgt-viz intersect -r $inputMatrixR -q $inputMatrixQ -stest 10 $outputLocation 


