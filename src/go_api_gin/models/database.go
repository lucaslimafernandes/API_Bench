package models

import (
	"context"
	"log"
	"os"
	"time"

	"github.com/jackc/pgx/v5/pgxpool"
)

var DB *pgxpool.Pool

func ConnectDB() {

	var err error
	maxRetries := 5
	retryDelay := 10 * time.Second

	for retries := 0; retries <= maxRetries; retries++ {

		DB, err = pgxpool.New(context.Background(), os.Getenv("DB_URL"))
		if err == nil {
			log.Println("Connected to database")
			return
		}

		log.Fatalf("Failed to connect to the database: %s\n", err)
		time.Sleep(retryDelay)

	}

	log.Fatalln("Failed to connect to the database: %s\n", err)

}

func Migrate() {

	CreateTables()

}
