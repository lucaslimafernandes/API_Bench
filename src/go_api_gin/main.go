package main

import (
	"github.com/gin-gonic/gin"
	"github.com/lucaslimafernandes/API_gin/controllers"
	"github.com/lucaslimafernandes/API_gin/models"
)

func init() {

	models.ConnectDB()
	models.CreateTables()
	models.CreateUser()

}

func main() {

	router := gin.Default()

	router.GET("/ping", controllers.Ping)

	// router.POST("/auth/signup")
	router.POST("/auth/login")

	router.Run(":3000")
}
