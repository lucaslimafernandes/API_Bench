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

	gin.SetMode(gin.ReleaseMode)

	router := gin.Default()

	router.GET("/ping", controllers.Ping)

	router.GET("/auth/login", controllers.Login)

	router.Run(":3000")

}
