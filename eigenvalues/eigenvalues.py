import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    import numpy as np

def calculate_eigenvalues(matrix):
    try:
        matrix = np.array(matrix, dtype=float)

        # Handle empty matrix
        if matrix.size == 0:
            return None

        # Must be 2D and square
        if len(matrix.shape) != 2:
            return None

        rows, cols = matrix.shape

        if rows != cols:
            return None

        eigenvalues = np.linalg.eigvals(matrix)

        # Sort by real part, then imaginary part
        eigenvalues = np.array(
            sorted(eigenvalues, key=lambda x: (x.real, x.imag))
        )

        return eigenvalues

    except Exception:
        return None