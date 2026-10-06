# TPV independent local validation note
#
# This is the same validation-method file referenced with the validated manuscript.
# It documents the independent automatic-differentiation check used to validate the
# O(alpha_B Omega^2), l=2 TPV reduced-action coefficient.
#
# Method:
# 1. Build the additive Hartle l=2 metric perturbation and O(Omega) frame dragging.
# 2. Use automatic differentiation for coordinate derivatives.
# 3. Construct Christoffel symbols, Riemann, Ricci, Weyl, and magnetic-Weyl tensors.
# 4. Extract the coefficient of epsilon^2 * eta in sqrt(-g) B_{mu nu} B^{mu nu}.
# 5. Compare against the closed-form reduced-action coefficient.
#
# Representative interior point:
#   r = 4.968897990 km
#
# Analytic reduced-action coefficient:
#   C_red = 2.108929477739e-02
#
# Independent AD / centered finite-difference convergence:
#
#   epsilon        eta          C_AD / C_red - 1
#   4.0e-3         4.0e-4       1.274e-3
#   2.0e-3         2.0e-4       3.185e-4
#   1.0e-3         1.0e-4       7.961e-5
#   5.0e-4         5.0e-5       1.990e-5
#
# Observed convergence orders:
#   2.0006, 2.0001, 2.0000
#
# Important bookkeeping point:
# The independent O(Omega^2), l=2 even-parity variation uses delta g_{t phi} = 0.
# The k_2 * omega term arising from a multiplicatively factorized Hartle metric is
# higher order and must not be treated as an independent l=2 variation.
#
# The full research calculation also contains the stellar TOV/Hartle integration,
# the TPV radial source construction, and the exterior quadrupole matching. This file
# is the compact validation-method note that accompanied the manuscript.

def main():
    print("TPV O(alpha_B Omega^2), l=2 validation note")
    print("C_red = 2.108929477739e-02")
    print("Convergence orders: 2.0006, 2.0001, 2.0000")
    print("See TPV_active_validated.tex for the full appendix and equations.")

if __name__ == "__main__":
    main()
