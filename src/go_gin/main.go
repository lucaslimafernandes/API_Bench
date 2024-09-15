package main

import (
	"github.com/gin-gonic/gin"
	"github.com/lucaslimafernandes/API_Bench/controllers"
	"github.com/lucaslimafernandes/API_Bench/models"
)

func init() {

	gin.SetMode(gin.ReleaseMode)

	models.ConnectDB()
	models.CreateTables()
	models.CreateUser()

}

func main() {

	router := gin.Default()

	router.GET("/ping", controllers.Ping)

	router.GET("/auth/login", controllers.Login)

	router.Run(":3000")

}
