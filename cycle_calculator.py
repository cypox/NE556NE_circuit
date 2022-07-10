import math

"""
Duty cycle calculator for NE556N Oscilator circuit
Use application 4.1 from the datasheet
"""

def t2(a, b, c):
  return ((a*b)/(a+b))*c*math.log((b-2*a)/(2*b-a))

def t1(a, c):
  return 0.693 * a * c

def f(t1, t2):
  return 1./(t1+t2)

def duty(t1, t2):
  return 100*t1/(t1+t2)

def cycle(a, b, c):
  T1 = t1(a, c)
  T2 = t2(a, b, c)
  print(f"t1={T1:.5f}s, t2={T2:.5f}s")
  print(f"f={f(T1,T2):.2f}Hz")
  print(f"d={duty(T1,T2):.2f}% (high to low)")

if __name__=="__main__":
  import sys
  if len(sys.argv) != 4:
    print("arguments are RA and RB in ohms and C in farads.")
    exit()
  RA = float(sys.argv[1])
  RB = float(sys.argv[2])
  C = float(sys.argv[3])
  cycle(RA, RB, C)

