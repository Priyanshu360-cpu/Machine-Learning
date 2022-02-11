package main

import (
	"fmt"

	. "github.com/go-opencv/go-opencv/gocv"
	"github.com/gonum/matrix/mat64"
)

func main() {

	objPts := mat64.NewDense(4, 3, []float64{
		0, 25, 0,
		0, -25, 0,
		-47, 25, 0,
		-47, -25, 0})

	imgPts := mat64.NewDense(4, 2, []float64{
		1136.4140625, 1041.89208984,
		1845.33190918, 671.39581299,
		302.73373413, 634.79998779,
		1051.46154785, 352.76107788})

	camMat := GcvInitCameraMatrix2D(objPts, imgPts)
	fmt.Println(camMat)
}
