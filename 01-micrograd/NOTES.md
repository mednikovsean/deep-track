# Build 1: micrograd
- the gradient of the parameter is the derivative of the output (the loss in training a model) with respect to that parameter. it tells the rate and direction at which the output changes when that parameters value is nudged
- a mathematical depiction of a neuron includes a certain number of inputs to the neuron as well as weights that interact with each input. we multiply each input to its corresponding weight, these are then added together along with the bias of the neuron itself. this comprises the data value of the neuron. the output of the neuron passes this sum through an activation squashing function like tanh
- backpropogation is the method of finding the derivative (which is the gradient) of the output with respect to everyone of its inputs. we always start by finding the derivative of the output with respect to itself which is 1, we then fill in backwards (most confusing)

BUGS I HIT:
__sub__ multiples instead of adding
__pow__ derivative has parantheses in wrong place
removed node incorrectly from visited set in topological sort build function

