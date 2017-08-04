package main

import (
    "bufio"
    "strings"
    "fmt"
    "os"
    "unicode"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    layoutA, _ := reader.ReadString('\n')
    layoutB, _ := reader.ReadString('\n')
    text, _ := reader.ReadString('\n')

    mappingA := make(map[rune]int)
    lettersA := strings.Split(layoutA, "")
    for i, s := range lettersA {
        for _, c := range s {
            mappingA[c] = i
        }
    }
    var lettersB []rune
    lettersB = make([]rune, len(lettersA), len(lettersA))
    for i, s := range strings.Split(layoutB, "") {
        for _, c := range s {
            lettersB[i] = c
        }
    }

    for _, c := range text {
        if unicode.IsDigit(c) {
            fmt.Printf("%c", c)
        } else if unicode.IsUpper(c) {
            j := mappingA[unicode.ToLower(c)]
            fmt.Printf("%c", unicode.ToUpper(lettersB[j]))
        } else {
            j := mappingA[c]
            fmt.Printf("%c", lettersB[j])
        }
    }

}
