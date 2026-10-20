# Learning Roadmap

The sequence prioritizes mathematical understanding and independent implementation. A topic is complete when it can be explained, coded, tested, and connected to a meaningful ML/AI application—not merely when its notebook has been opened.

## Phase 1 — Linear Algebra

1. **Vectors:** notation, components, dimensions, vector arithmetic, dot product, norms, cosine similarity.
2. **Vector geometry:** angles, unit vectors, orthogonality, projections, distances.
3. **Matrices:** shape, transpose, matrix-vector and matrix-matrix multiplication, identity and inverse.
4. **Linear systems:** $Ax=b$, elimination, pivots, rank, consistency, solution sets.
5. **Vector spaces:** span, independence, basis, dimension, column space, null space, rank-nullity.
6. **Linear transformations:** matrix representation, composition, change of basis.
7. **Orthogonality and least squares:** projection, Gram–Schmidt, QR, least-squares solutions.
8. **Eigenvalues and eigenvectors:** characteristic equations, diagonalization, symmetric matrices.
9. **Matrix decompositions:** LU, QR, eigendecomposition, SVD; applications to PCA.

## Phase 2 — Statistics and Probability

- Descriptive statistics, random variables, expectation, variance, common distributions.
- Covariance, correlation, conditional probability, Bayes' rule, sampling, and uncertainty.
- Numerical simulation to check theoretical expectations.

## Phase 3 — Calculus and Optimization

- Limits and derivatives review, partial derivatives, gradients, chain rule.
- Jacobians, Hessians, loss functions, gradient descent, learning rates, conditioning, and convergence intuition.
- Visualize optimization behavior and implement gradient descent from scratch.

## Phase 4 — Applied Machine Learning

- Data cleaning, exploratory analysis, feature engineering, train/validation/test splits.
- Regression, classification, model metrics, cross-validation, pipelines, and leakage prevention.
- Build reproducible projects using real datasets, with limitations and evaluation documented.

## Phase 5 — Deep Learning foundations

- Tensors, automatic differentiation, neural-network layers, loss functions, optimizers, training loops.
- Train and evaluate at least one small neural network; explain the model and its limitations.

## Definition of done for a topic

- [ ] Markdown notes explain the concept, notation, assumptions, and a worked example.
- [ ] The learner independently implemented the central idea in Python where appropriate.
- [ ] A NumPy/SciPy comparison or verification is included where appropriate.
- [ ] Exercises were attempted independently and explained.
- [ ] Input validation, shapes, and numerical edge cases were considered.
- [ ] The notebook runs top-to-bottom from a fresh kernel.
- [ ] Reusable logic has automated tests.
- [ ] Documentation and the progress tracker are updated.
- [ ] A focused Git commit records the actual work completed.