package models

import (
	"context"
	"log"
	"time"

	"golang.org/x/crypto/bcrypt"
)

type User struct {
	ID        uint      `json:"id"`
	Email     string    `json:"email"`
	Fullname  string    `json:"fullname"`
	Password  string    `json:"password"`
	CreatedAt time.Time `json:"created_at"`
}

func CreateTables() {

	sql_query := `
		CREATE TABLE IF NOT EXISTS users (
			id SERIAL PRIMARY KEY,
			email VARCHAR(255) UNIQUE NOT NULL,
			fullname VARCHAR(255) NOT NULL,
			password VARCHAR(255) NOT NULL,
			created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
		);
	`

	_, err := DB.Exec(context.Background(), sql_query)
	if err != nil {
		log.Fatalf("Failed to create users table: %s\n", err)
	}

}

func CreateUser() {

	var userFound User
	userCreate := User{
		Email:    "test@test.com",
		Fullname: "Joey Tribbiani",
		Password: "password123",
	}

	query := "select id from users where email=$1"
	insertQuery := `
		INSERT INTO users (email, fullname, password, created_at)
		VALUES ($1, $2, $3, $4)
		RETURNING id
	`

	DB.QueryRow(context.Background(), query, userCreate.Email).Scan(
		&userFound.ID,
	)

	if userFound.ID == 0 {

		passwordHash, _ := bcrypt.GenerateFromPassword([]byte(userCreate.Password), bcrypt.DefaultCost)

		user := User{
			Email:    userCreate.Email,
			Fullname: userCreate.Fullname,
			Password: string(passwordHash),
		}

		err := DB.QueryRow(context.Background(), insertQuery, user.Email, user.Fullname, user.Password, time.Now()).Scan(&user.ID)
		if err != nil {
			log.Fatalf("Failed to insert new user: %v\n", err)
		}

		log.Printf("User created with ID: %d\n", user.ID)
	} else {
		log.Println("User already exists")
	}

}
