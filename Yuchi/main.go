package main

import "fmt"

type Node struct {
	val  int   // 節點的値
	next *Node // 下一個節點
}

type LinkList struct {
	head *Node
}

func isEmpty(LL *LinkList) bool {
	return LL.head == nil
}

func length(LL *LinkList) int {
	if isEmpty(LL) {
		return 0
	} else {
		temp := LL.head
		count := 1
		for {
			if temp.next != nil {
				temp = temp.next
				count++
			} else {
				break
			}
		}
		return count
	}
}

func show(LL *LinkList) {
	temp := LL.head
	for i := 0; i < length(LL); i++ {
		fmt.Printf("%d, ", temp.val)
		temp = temp.next
	}
	fmt.Print("\n")
}

func add(LL *LinkList, val int) {
	n := Node{
		val: val,
	}
	n.next = LL.head
	LL.head = &n
}

func append(LL *LinkList, val int) {
	if isEmpty(LL) {
		add(LL, val)
	} else {
		n := Node{
			val: val,
		}
		temp := LL.head

		for {
			if temp.next != nil {
				temp = temp.next
			} else {
				break
			}
		}
		temp.next = &n
	}
}

func search(LL *LinkList, val int) int {
	if isEmpty(LL) {
		return -1
	} else {
		temp := LL.head
		count := 0
		for {
			if temp != nil { // head不為空才能找
				if temp.val == val { // 找到
					return count
				} else if temp.next != nil { // 沒找到，下一個不為空
					temp = temp.next
					count++
				}
			} else { // head為空不能找
				break
			}
		}
		return -1
	}
}

func insert(LL *LinkList, pos int, val int) {
	if pos == 0 { // 位置0，加在最前面
		add(LL, val)
	} else if length(LL) < pos { // 位置超出長度，加在最後面
		append(LL, val)
	} else if pos < 0 {
		fmt.Println("你是不是沒被打過")
	} else {
		temp := LL.head
		for i := 0; i < pos-1; i++ {
			temp = temp.next
		}
		n := Node{
			val: val,
		}
		n.next = temp.next
		temp.next = &n
	}
}

func delete(LL *LinkList, val int) {
	if !isEmpty(LL) {
		temp := LL.head
		if temp.val == val { // 如果head就是該値
			LL.head = temp.next
		} else {
			for {
				if temp.next == nil {
					fmt.Println("沒這個値可以刪除")
					break
				} else if temp.next.val != val {
					temp = temp.next
					continue
				} else {
					temp.next = temp.next.next
					break
				}
			}
		}
	}
}

func main() {
	a := Node{
		val: 5,
	}
	linklist := LinkList{
		head: &a,
	}
	add(&linklist, 7)
	add(&linklist, 9)
	append(&linklist, 10)
	append(&linklist, 11)

	show(&linklist)
	delete(&linklist, 10)
	show(&linklist)
}
