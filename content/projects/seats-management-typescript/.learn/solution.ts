const ROWS = 8;
const COLUMNS = 10;

function createSeatingMatrix(rows: number, columns: number): number[][] {
  const matrix: number[][] = [];
  for (let i = 0; i < rows; i++) {
    const row: number[] = [];
    for (let j = 0; j < columns; j++) {
      row.push(0); // 0 means available
    }
    matrix.push(row);
  }
  return matrix;
}

function printSeating(matrix: number[][]): void {
  console.log("Current seating map (X = occupied, L = free)");

  let header = "   ";
  for (let col = 0; col < matrix[0].length; col++) {
    header += String(col + 1).padStart(2, " ") + " ";
  }
  console.log(header);

  for (let row = 0; row < matrix.length; row++) {
    let line = String(row + 1).padStart(2, " ") + " ";
    for (let col = 0; col < matrix[row].length; col++) {
      const seat = matrix[row][col] === 1 ? "X" : "L";
      line += ` ${seat} `;
    }
    console.log(line);
  }
}

function reserveSeat(matrix: number[][], row: number, column: number): string {
  const rowIndex = row - 1;
  const colIndex = column - 1;

  if (
    rowIndex < 0 ||
    rowIndex >= matrix.length ||
    colIndex < 0 ||
    colIndex >= matrix[0].length
  ) {
    return "Selected seat is out of range.";
  }

  if (matrix[rowIndex][colIndex] === 1) {
    return `Seat (${row}, ${column}) is already occupied.`;
  }

  matrix[rowIndex][colIndex] = 1;
  return `Seat (${row}, ${column}) has been reserved.`;
}

function countSeats(matrix: number[][]): { occupied: number; available: number } {
  let occupied = 0;
  let available = 0;

  for (let row = 0; row < matrix.length; row++) {
    for (let col = 0; col < matrix[row].length; col++) {
      if (matrix[row][col] === 1) {
        occupied++;
      } else {
        available++;
      }
    }
  }

  return { occupied, available };
}

function findAdjacentSeats(matrix: number[][]): [number, number][] | null {
  for (let row = 0; row < matrix.length; row++) {
    for (let col = 0; col < matrix[row].length - 1; col++) {
      const first = matrix[row][col];
      const second = matrix[row][col + 1];

      if (first === 0 && second === 0) {
        return [
          [row + 1, col + 1],
          [row + 1, col + 2],
        ];
      }
    }
  }

  return null;
}

function demo(): void {
  const seating = createSeatingMatrix(ROWS, COLUMNS);

  console.log("Initial room (all seats available):");
  printSeating(seating);

  console.log(reserveSeat(seating, 1, 1));
  console.log(reserveSeat(seating, 1, 2));
  console.log(reserveSeat(seating, 4, 5));
  console.log(reserveSeat(seating, 4, 6));

  console.log("\nAfter some reservations:");
  printSeating(seating);

  const counts = countSeats(seating);
  console.log("occupied", counts.occupied);
  console.log("available", counts.available);

  const adjacent = findAdjacentSeats(seating);
  if (adjacent) {
    const [first, second] = adjacent;
    console.log(
      `First pair of adjacent seats found at (${first[0]}, ${first[1]}) and (${second[0]}, ${second[1]}).`
    );
  } else {
    console.log("No pair of adjacent available seats found.");
  }
}

demo();
