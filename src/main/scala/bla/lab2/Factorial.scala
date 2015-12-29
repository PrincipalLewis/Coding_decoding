package bla.lab2
class Factorial() {
  private def undo(x: Int, fact: Int, count: Int, res: Int) : Int = {
    if ((x / 10)==0) {
      res + x * fact
    } else {
      undo(x / 10, fact * (count+1), count+1, res + (x % 10) * fact)
    }
  }

  def un(x: Int) : Int = {
    undo(x, 1, 1, 0)
  }

  private def todo(x: Int, count: Int, res: List[Int]) : List[Int] = {
    if ((x / count) == 0) {
      (x % count) :: res
    } else {
      todo(x / count, count+1,(x % count) :: res)
    }
  }

  def to(x: Int) : List[Int] = {
    todo(x,2,List())
  }
}
