package main

import (
	"errors"
	"fmt"
)

// get_int_generator はint型の値を返すジェネレータを返す関数
func get_int_generator() func() (int, error) {
	// テスト用のint型配列を定義する
	myarray := [...]int{10, 20, 30}
	// インデックスの添字を初期化
	index := -1
	// int型またはerror型を返す無名ジェネレータ関数を返却する
	// func() (int, error) {
		// 次のインデックスの添字を取得する
		index++
		// インデックスが配列を全て参照した場合はエラーを返して終了
		if index >= len(myarray) {
			return 0, errors.New("配列に値が存在しません")
		}
		// 配列内の指定したインデックスの値を返す
		return myarray[index], nil
	}
}

func main() {
	// 状態を保持するクロージャ関数を取得する
	generator := get_int_generator()
	
	// var twiced_generator = map(lambda x: x * 2, generator) 的なことができる
	// これだと最後に余計な 0 , が実行されるがシンプルに加工処理を書ける
	twiced_generator := func() (int, error) {
		value, err := generator()
		return value * 2, err
	}
	
	// for value in twiced_generator() みたいなことをするための記述
	for {
		// ループを抜けるまでジェネレータ関数が実行され新たな値が取得される
		value, err := againd_generator()
	if err != nil {
			break
		}
		// 返却値があれば表示する
		fmt.Println(value)
	}
	fmt.Println("ループ終了")
}
