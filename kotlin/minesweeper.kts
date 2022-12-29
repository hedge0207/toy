import kotlin.random.Random


class MineField(var totalMine: Int) {
    val N = 9
    val mineField = MutableList(N) { MutableList(N) { '/' } }
    val playField = MutableList(N) { MutableList(N) { '.' } }
    var numsMine: Int = 0
    val coordinates = mutableListOf<Int>(-1, 0, 1)

    fun createMineField() {
        while (totalMine > numsMine) {
            val row = Random.nextInt(0, 9)
            val col = Random.nextInt(0, 9)
            if (mineField[row][col] != '*') {
                mineField[row][col] = '*'
                numsMine++
                countNumNearMine(row, col)
            } else {
                continue
            }
        }
    }

    fun countNumNearMine(row: Int, col: Int) {
        for (i in -1..1) {
            val newRow = row + i
            if (newRow in 0 until N) {
                for (j in -1..1) {
                    val newCol = col + j
                    if (newCol in 0 until N) {
                        if (mineField[newRow][newCol] == '*') {
                            continue
                        }
                        if (mineField[newRow][newCol] == '/') {
                            mineField[newRow][newCol] = '0'
                        }
                        var numNearMine = mineField[newRow][newCol].code
                        numNearMine++
                        mineField[newRow][newCol] = numNearMine.toChar()
                    }
                }
            }
        }
    }

    fun printPlayField() {

        println(" |123456789|")
        println("-|---------|")
        var cnt = 0
        for (row in playField) {
            cnt++
            print("$cnt|")
            print(row.joinToString(""))
            println("|")
        }
        println("-|---------|")
    }

    fun clearArea(x: Int, y: Int) {
        if (x < 0 || x >= N || y < 0 || y >= N) {
            return
        }
        if (mineField[x][y].isDigit()) {
            playField[x][y] = mineField[x][y]
        }
        if ((playField[x][y] == '.' && mineField[x][y] == '/') || (playField[x][y] == '*' && mineField[x][y] != '*')) {
            playField[x][y] = '/'
            for (i in coordinates) {
                for (j in coordinates) {
                    if (i == 0 && j == 0) {
                        continue
                    }
                    clearArea(x + i, y + j)
                }
            }
        }
    }

    fun gameOver() {
        for (i in 0 until N) {
            for (j in 0 until N) {
                if (mineField[i][j] == '*') {
                    playField[i][j] = 'X'
                }
            }
        }
        printPlayField()
    }

    fun checkClear(): Boolean {
        var remainCell = 0
        var foundMine = 0
        for (row in 0 until N) {
            for (col in 0 until N) {
                if (playField[row][col] == '.') {
                    remainCell++
                }
                if (playField[row][col] == '*' && mineField[row][col] == '*') {
                    foundMine++
                }
            }
        }
        return remainCell == totalMine || foundMine == totalMine || foundMine == remainCell + totalMine
    }

    fun markMine(x:Int, y:Int) {
        if (playField[x][y] == '*') {
            playField[x][y] = '.'
        } else {
            playField[x][y] = '*'
        }
        printPlayField()
    }

    fun play() {
        while (true) {
            print("Set/delete mines marks (x and y coordinates):")
            var coordinates = readln().split(" ")
            val y = coordinates[0].toInt() - 1
            val x = coordinates[1].toInt() - 1
            val type = coordinates[2]

            if (type == "mine") {
                markMine(x, y)
                continue
            }

            if (mineField[x][y] == '*') {
                gameOver()
                println("You stepped on a mine and failed!")
                break
            }

            clearArea(x, y)

            printPlayField()

            if (checkClear()) {
                println("Congratulations! You found all the mines!")
                break
            }
        }
    }
}

fun main() {
    print("How many mines do you want on the field? ")
    val totalMine = readln().toInt()
    val mineField = MineField(totalMine)
    mineField.createMineField()
    mineField.printPlayField()
    mineField.play()
}

main()