package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("rule not input")
		os.Exit(1)
	}

	rulePathList := getUserRulePath()
	for _, v := range rulePathList {
		writeNewRule(v)
	}
}

func getCurrentDir() string {
	path, _ := os.Executable()
	return filepath.Dir(path)
}

func getUserRulePath() []string {
	configPath := filepath.Join(getCurrentDir(), "config.txt")
	fd, err := os.Open(configPath)
	if err != nil {
		fmt.Println(err)
		return nil
	}

	reader := bufio.NewReader(fd)
	var result []string
	for {
		b, _, err := reader.ReadLine()
		if err != nil {
			if err == io.EOF {
				if len(result) == 0 {
					fmt.Println("config file is empty")
				}
				return result
			}

			fmt.Println(err)
			return nil
		}

		filePath := strings.TrimSpace(string(b))
		if filePath == "" {
			continue
		}
		result = append(result, filePath)
	}
}

func writeNewRule(filePath string) {
	rule := os.Args[1]
	fd, err := os.OpenFile(filePath, os.O_WRONLY|os.O_CREATE|os.O_APPEND, os.ModePerm)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	fd.WriteString("\r\n" + "*" + rule + "*")
	fd.Close()
}
