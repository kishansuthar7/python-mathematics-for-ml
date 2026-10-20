# Python Mathematics for Machine Learning

A Jupyter Notebook-first learning repository that connects mathematical concepts with Python implementations, NumPy verification, and practical machine-learning applications.

The goal is to understand the mathematics, implement algorithms independently, verify results, test edge cases, and document the learning process clearly.

## Learning Goals

- Strengthen the mathematics used in Machine Learning and Artificial Intelligence.
- Implement mathematical operations using pure Python.
- Verify implementations using NumPy.
- Understand array dimensions, shapes, numerical calculations, and edge cases.
- Maintain clean, reusable code with automated tests.
- Build a genuine, topic-wise GitHub learning portfolio.

## Repository Structure

```text
python-mathematics-for-ml/
|-- README.md
|-- pyproject.toml
|-- requirements.txt
|-- .gitignore
|-- docs/
|   |-- learning_roadmap.md
|   `-- references.md
|-- notebooks/
|   `-- 01_linear_algebra/
|       |-- 01_vectors.ipynb
|       `-- 01_vectors_exercises.ipynb
|-- src/
|   `-- mathml/
|       `-- linear_algebra/
|           `-- vectors.py
|-- tests/
|   `-- test_vectors.py
`-- data/
    |-- raw/
    `-- processed/
```

## Current Learning Milestone: Vectors

The vector module covers:

- Vector addition and subtraction
- Scalar multiplication
- Dot product
- Euclidean magnitude (L2 norm)
- Cosine similarity
- Input validation and edge cases
- NumPy verification and automated testing

The implementation is maintained in `src/mathml/linear_algebra/vectors.py`.

The tests are maintained in `tests/test_vectors.py`.

## Learning Workflow

For each topic:

1. Read the mathematical explanation and understand the notation.
2. Derive the formula using a small example.
3. Implement the operation using Python.
4. Verify the result using NumPy.
5. Test normal cases and edge cases.
6. Refactor reusable functions into `src/`.
7. Document the results and publish a meaningful Git commit.

## Setup in VS Code on Windows

This project can use the existing virtual environment at:

`Documents/JupyterWorkspace/.venv`

Open the `python-mathematics-for-ml` folder itself in VS Code.

From the project root, install the project and its development dependencies:

```powershell
& "$HOME\Documents\JupyterWorkspace\.venv\Scripts\python.exe" -m pip install -e ".[dev]"
```

Adjust the path if your virtual environment is stored elsewhere.

### Open the notebooks

1. Open `notebooks/01_linear_algebra/01_vectors.ipynb`.
2. Select the Python interpreter associated with your virtual environment.
3. Run the notebook cells in order.
4. Complete the exercises and verify their outputs.

## Run Automated Tests

From the project root, run:

```powershell
& "$HOME\Documents\JupyterWorkspace\.venv\Scripts\python.exe" -m pytest -v
```

The current vector test suite contains 10 tests. All 10 passed during the latest verified run. Run the tests again after making code changes.

## Notebook Formatting

Use `$...$` for inline mathematics and `$$...$$` for display equations.

Avoid complex LaTeX expressions inside Markdown table cells. Use a separate equation block when a formula needs more space.

## Upcoming Topics

- Matrices and matrix operations
- Systems of linear equations
- Vector spaces, span, basis, and rank
- Linear transformations
- Orthogonality and least squares
- Eigenvalues and eigenvectors
- Matrix decompositions and Singular Value Decomposition
- Probability and statistics
- Calculus and optimization
- Applied Machine Learning projects

## References

- [Mathematics for Machine Learning](https://mml-book.github.io/)
- [MIT OpenCourseWare: Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [scikit-learn Getting Started](https://scikit-learn.org/stable/getting_started.html)
- [PyTorch Tutorials](https://docs.pytorch.org/tutorials/)

## Data and Responsible Use

Do not commit passwords, API tokens, private information, or large datasets without appropriate permission.

The `.gitignore` file excludes virtual environments, generated files, caches, and raw or processed data files by default.
