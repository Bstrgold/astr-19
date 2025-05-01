{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5af812b3-fdb0-439f-8e21-6688c3980c64",
   "metadata": {},
   "source": [
    "# Sine and Cosine Function Tabulation\n",
    "\n",
    "In this notebook, we define and use functions for `sin(x)` and `cos(x)`, tabulate them over the interval `[0, 2]` with 1000 entries, and display the first 10 results."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a099831e-45ef-4a5c-811e-3b4af984443d",
   "metadata": {},
   "source": [
    "### sin_function(x)\n",
    "\n",
    "This function takes a value `x` as input and returns `sin(x)` using Python's built-in `math.sin()` function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b344540d-06fb-45f4-8414-816b1ee00845",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "def sin_function(x):\n",
    "    \"\"\"\n",
    "    Returns the sine of x.\n",
    "    \"\"\"\n",
    "    return math.sin(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d1c7fef3-bb53-40c6-91f0-a29d4200a324",
   "metadata": {},
   "source": [
    "### cos_function(x)\n",
    "\n",
    "This function takes a value `x` as input and returns `cos(x)` using Python's built-in `math.cos()` function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cf22a1fb-eb2d-4820-9227-ce8253ae7d65",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cos_function(x):\n",
    "    \"\"\"\n",
    "    Returns the cosine of x.\n",
    "    \"\"\"\n",
    "    return math.cos(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d002cdf2-bfbf-4e33-8b0c-08cffc99857f",
   "metadata": {},
   "source": [
    "### Tabulate sin(x) and cos(x) \n",
    "\n",
    "using these previously defined functions vs. x, where x is tabulated between 0 and 2 with a thousand entries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c5a22914-2e91-4667-bdd5-3819d757da8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "num_points = 1000\n",
    "start = 0\n",
    "end = 2\n",
    "step = (end - start) / (num_points - 1)\n",
    "\n",
    "x_values = [start + i * step for i in range(num_points)]\n",
    "sin_values = [sin_function(x) for x in x_values]\n",
    "cos_values = [cos_function(x) for x in x_values]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e954103e-b95e-4afd-94e1-f2956cd46594",
   "metadata": {},
   "source": [
    "### Print First 10 Values\n",
    "\n",
    "Use a loop to print the first 10 values of `x`, `sin(x)`, and `cos(x)` side by side in column format."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "076dcf6c-c870-4af6-802a-402082b0ec7f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         x          sin(x)          cos(x)\n",
      "----------------------------------------\n",
      "  0.000000        0.000000        1.000000\n",
      "  0.002002        0.002002        0.999998\n",
      "  0.004004        0.004004        0.999992\n",
      "  0.006006        0.006006        0.999982\n",
      "  0.008008        0.008008        0.999968\n",
      "  0.010010        0.010010        0.999950\n",
      "  0.012012        0.012012        0.999928\n",
      "  0.014014        0.014014        0.999902\n",
      "  0.016016        0.016015        0.999872\n",
      "  0.018018        0.018017        0.999838\n"
     ]
    }
   ],
   "source": [
    "print(f\"{'x':>10} {'sin(x)':>15} {'cos(x)':>15}\")\n",
    "print(\"-\" * 40)\n",
    "for i in range(10):\n",
    "    print(f\"{x_values[i]:10.6f} {sin_values[i]:15.6f} {cos_values[i]:15.6f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "80d515b8-d4a1-40ad-83aa-e8141dadffc2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
