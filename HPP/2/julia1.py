"""Julia set generator without optional PIL-based image drawing"""

import calculate

# area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193
    
def calc_pure_python(desired_width, max_iterations):
    """Create a list of complex coordinates (zs) and complex
    parameters (cs), build Julia set, and display"""
    start_time = time.time()
    output = calculate.calculate_z(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print("Took", secs, "seconds")
    assert sum(output) == 33219980

if __name__ == "__main__":
    # Calculate the Julia set using a pure Python solution with
    # reasonable defaults for a laptop
    calc_pure_python(desired_width=1000, max_iterations=300)
