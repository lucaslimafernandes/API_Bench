package controllers

import (
	"context"
	"net/http"
	"os"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/golang-jwt/jwt/v4"
	"github.com/jackc/pgx/v5"
	"github.com/lucaslimafernandes/API_gin/models"
	"golang.org/x/crypto/bcrypt"
)

func Login(c *gin.Context) {

	var userFound models.User

	authInput := models.User{
		Email:    "test@test.com",
		Password: "password123",
	}

	query := "SELECT id, email, fullname, password, created_at FROM users WHERE email=$1"

	err := models.DB.QueryRow(context.Background(), query, authInput.Email).Scan(
		&userFound.ID,
		&userFound.Email,
		&userFound.Fullname,
		&userFound.Password,
		&userFound.CreatedAt,
	)

	if err != nil {
		if err == pgx.ErrNoRows {
			c.JSON(http.StatusBadRequest, gin.H{"error": "user not found"})
		} else {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "database error"})
		}
		return
	}

	err = bcrypt.CompareHashAndPassword([]byte(userFound.Password), []byte(authInput.Password))
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "invalid password"})
		return
	}

	generateToken := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
		"id":  userFound.ID,
		"exp": time.Now().Add(time.Hour * 24).Unix(),
	})

	token, err := generateToken.SignedString([]byte(os.Getenv("SECRET")))
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "failed to generate token"})
		return
	}

	c.JSON(http.StatusOK, gin.H{"token": token})

}
