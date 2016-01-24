package bla.lab2


class Fibonachi() {

  var fibonachi:List[Int] = List(1,2,3,5,8,13,21,34)
  def undo(x: Int, fib: List[Int], res: Int) : Int = {
    if ((x / 10)==0) {
      res + (x % 10) * fib.head
    } else {
      undo(x / 10, fib.tail, res + (x % 10) * fib.head)
    }
  }

  def un(x: Int) : Int = {
    undo(x, fibonachi, 0)
  }

  def todo(x: Int, fib: List[Int], res: List[Int], i: Int) : List[Int] = {
    if (i < 0) {
      return res.reverse
    }
    if (x >= fibonachi(i)) {
      todo(x-fibonachi(i), fibonachi, 1 :: res, i-1)
    } else {
      todo(x, fibonachi, 0 :: res, i-1)
    }
  }

  def to(x: Int) : List[Int] = {
    var i = fibonachi.length-1
    while (x < fibonachi(i)) {
      i = i-1
    }

    todo(x, fibonachi, List(), i)
  }
}

