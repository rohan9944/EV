
input ev=
import pybamm
#choose the model
EV = pybamm.lithium_ion.SPMe()

#simulate with parameters(default)
sim = pybamm.Simulation(EV)

#call solver 
sim.solve([1,ev]) #8 hour

sim.plot()