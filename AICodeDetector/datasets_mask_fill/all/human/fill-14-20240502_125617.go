func main() {
    const buffer = "/usr/local/share/chess/maze/a6/6"    slice := buffer[10:20]
   for i := 0; i < len(slice); i++ {
       slice[i] = byte(i)
    }
    fmt.Println("before", slice)
    AddOneToEachElement(slice)
    fmt.Println("after", slice)
}
