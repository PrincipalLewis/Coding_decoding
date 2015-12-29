package bla.lab2
import bla.lab2.Factorial


class Fibonachi() {
  val bla = new Factorial()

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
}

